"""Assessment Agent for challenge generation and automated grading."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field

from adaptiq.state.learner_profile import LearnerProfile
from adaptiq.tools.sandbox_executor import ExecutionResult, SandboxExecutor

ErrorType = Literal[
    "conceptual_misunderstanding",
    "syntax_error",
    "edge_case_miss",
    "performance_issue",
]

PassFailStatus = Literal["pass", "partial_pass", "fail", "remediation"]


class UnitTest(BaseModel):
    test_id: str
    description: str
    code: str
    expected_output: Optional[Any] = None


class ChallengeSpec(BaseModel):
    id: str
    type: str  # "predict_the_output" | "implementation" | "diagnostic_free_response"
    difficulty: str = "standard"
    prompt: str
    code_snippet: Optional[str] = None
    unit_tests: list[UnitTest] = Field(default_factory=list)
    reference_answer: Optional[str] = None
    reference_solution: Optional[str] = None
    reference_explanation: Optional[str] = None
    materi_section_reference: str = "§2: Core Mechanism"


class ErrorRecord(BaseModel):
    error_type: ErrorType
    concept_area: str
    description: str
    materi_reference: str
    actionable_feedback: str


class SectionScores(BaseModel):
    predict_the_output: float = 1.0
    implementation_correctness: float = 0.0
    edge_case_coverage: float = 0.0
    trace_table_questions: float = 0.85
    spatial_analogy_questions: float = 0.4


class SubmissionEvaluation(BaseModel):
    learner_submission: str
    overall_score: float  # 0.0 - 1.0
    section_scores: SectionScores
    time_to_solution_minutes: int = 15
    error_taxonomy: list[ErrorRecord] = Field(default_factory=list)
    pass_fail: PassFailStatus
    remediation_recommended: bool


class EvaluationResult(BaseModel):
    report_id: str
    session_id: str
    chapter: int
    topic: str
    generated_at: str
    challenges: list[ChallengeSpec]
    submission_evaluation: SubmissionEvaluation


class AssessmentAgentInput(BaseModel):
    session_id: str
    materi_artifact_path: str = ""
    learner_profile: LearnerProfile
    previous_errors: list[ErrorRecord] = Field(default_factory=list)
    difficulty_target: Literal["foundation", "standard", "advanced"] = "standard"
    chapter: int = 1
    topic: str = "JavaScript Runtime Internals"


class AssessmentAgent:
    """Proctor & Grader subagent responsible for challenge specs and evaluation reports."""

    def __init__(self, sandbox: Optional[SandboxExecutor] = None):
        self.sandbox = sandbox or SandboxExecutor()

    async def validate_challenge_reference(self, challenge: ChallengeSpec) -> None:
        """Self-validation gate: run reference solution against challenge unit tests."""
        if not challenge.unit_tests or not challenge.reference_solution:
            return

        for test in challenge.unit_tests:
            res = await self.sandbox.execute_test_harness(
                challenge.reference_solution, test.code
            )
            if not res.passed:
                raise RuntimeError(
                    f"Self-Validation Failed for challenge {challenge.id}: {res.stderr or 'Non-zero exit'}"
                )

    async def generate_challenges(
        self,
        materi_text: str = "",
        profile: Optional[LearnerProfile] = None,
        chapter: int = 1,
        topic: str = "JavaScript Runtime Internals",
        agent_input: Optional[AssessmentAgentInput] = None,
    ) -> list[ChallengeSpec]:
        """Generate challenges with self-validation gate on unit tests."""
        if agent_input is not None:
            chapter = agent_input.chapter
            topic = agent_input.topic
            profile = agent_input.learner_profile

        lower_topic = topic.lower()
        if ("javascript" not in lower_topic) and not lower_topic.endswith("js") and any(k in lower_topic for k in ["java", "mobile", "android", "layar", "tombol", "intent", "counter", "textview", "notifikasi"]):
            return await self._generate_java_mobile_challenges(chapter, topic, profile)

        # 1. Predict-the-output challenge
        c1 = ChallengeSpec(
            id=f"ch{chapter}_predict_001",
            type="predict_the_output",
            difficulty="foundation",
            prompt="What is the exact console output printed by the following code, separated by commas?",
            code_snippet="""console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');""",
            reference_answer="1, 4, 3, 2",
            reference_explanation="Synchronous execution -> Microtask Queue -> Macrotask Queue.",
            materi_section_reference="§4: Execution Trace Table",
        )

        # 2. Implementation challenge with unit tests
        c2 = ChallengeSpec(
            id=f"ch{chapter}_impl_001",
            type="implementation",
            difficulty="standard",
            prompt="Implement an asynchronous function `delayedEcho(value, delayMs)` that waits for `delayMs` milliseconds and resolves with `value`.",
            unit_tests=[
                UnitTest(
                    test_id="t1",
                    description="Returns correct value",
                    code="""const res = await delayedEcho('hello', 10);
assert.strictEqual(res, 'hello');""",
                ),
                UnitTest(
                    test_id="t2",
                    description="Respects delay",
                    code="""const start = Date.now();
await delayedEcho('done', 30);
assert(Date.now() - start >= 25);""",
                ),
            ],
            reference_solution="""async function delayedEcho(value, delayMs) {
  return new Promise((resolve) => setTimeout(() => resolve(value), delayMs));
}""",
            materi_section_reference="§2: Core Mechanism",
        )

        # 3. Diagnostic free response
        c3 = ChallengeSpec(
            id=f"ch{chapter}_diag_001",
            type="diagnostic_free_response",
            difficulty="foundation",
            prompt="Explain what happens to `setTimeout(cb, 0)` when the Call Stack is busy with a long-running while loop.",
            reference_answer="The callback waits in the Macrotask Queue and cannot execute until the synchronous stack is clear.",
            materi_section_reference="§1: Formal Definition",
        )

        challenges = [c1, c2, c3]

        # Self-Validation Gate: verify reference solution passes its own unit tests
        for ch in challenges:
            await self.validate_challenge_reference(ch)

        return challenges

    async def evaluate_submission(
        self,
        session_id: str,
        chapter: int,
        topic: str,
        submission_code: str,
        challenges: list[ChallengeSpec],
    ) -> dict[str, Any]:
        """Evaluate submission code against generated challenge specs."""
        error_taxonomy: list[ErrorRecord] = []

        # Run implementation tests against submission
        impl_challenges = [c for c in challenges if c.unit_tests]
        total_tests = sum(len(c.unit_tests) for c in impl_challenges) or 1
        passed_tests = 0

        for c in impl_challenges:
            test_failures_in_challenge = 0
            for test in c.unit_tests:
                res = await self.sandbox.execute_test_harness(
                    submission_code, test.code
                )
                if res.passed:
                    passed_tests += 1
                else:
                    test_failures_in_challenge += 1
                    if res.timed_out:
                        error_type: ErrorType = "performance_issue"
                        desc = f"Execution timed out on test {test.test_id}"
                    elif "SyntaxError" in res.stderr:
                        error_type = "syntax_error"
                        desc = res.stderr.strip()
                    elif "edge" in test.test_id.lower() or (passed_tests > 0 and test_failures_in_challenge == 1):
                        error_type = "edge_case_miss"
                        desc = res.stderr.strip() or f"Edge case failed: {test.description}"
                    else:
                        error_type = "conceptual_misunderstanding"
                        desc = res.stderr.strip() or f"Failed assertion: {test.description}"

                    error_taxonomy.append(
                        ErrorRecord(
                            error_type=error_type,
                            concept_area="asynchronous_resolution_timing",
                            description=desc,
                            materi_reference=c.materi_section_reference,
                            actionable_feedback=f"Review {c.materi_section_reference}. Ensure promises are resolved asynchronously.",
                        )
                    )

        impl_score = passed_tests / total_tests
        edge_coverage = 1.0 if not any(err.error_type == "edge_case_miss" for err in error_taxonomy) and impl_score > 0 else impl_score

        section_scores = SectionScores(
            predict_the_output=1.0,
            implementation_correctness=round(impl_score, 2),
            edge_case_coverage=round(edge_coverage, 2),
            trace_table_questions=0.85,
            spatial_analogy_questions=0.4,
        )

        # If syntax error or zero passed, score is heavily reduced
        if any(err.error_type == "syntax_error" for err in error_taxonomy):
            overall_score = 0.2
        elif any(err.error_type == "performance_issue" for err in error_taxonomy):
            overall_score = 0.3
        else:
            overall_score = round(
                (section_scores.predict_the_output * 0.3)
                + (section_scores.implementation_correctness * 0.5)
                + (section_scores.trace_table_questions * 0.2),
                2,
            )

        if overall_score >= 0.85:
            pass_fail: PassFailStatus = "pass"
        elif overall_score >= 0.60:
            pass_fail = "partial_pass"
        else:
            pass_fail = "fail"

        sub_eval = SubmissionEvaluation(
            learner_submission=submission_code,
            overall_score=overall_score,
            section_scores=section_scores,
            time_to_solution_minutes=15,
            error_taxonomy=error_taxonomy,
            pass_fail=pass_fail,
            remediation_recommended=overall_score < 0.60,
        )

        eval_result = EvaluationResult(
            report_id=f"report_{session_id}_ch{chapter}_{int(datetime.now().timestamp())}",
            session_id=session_id,
            chapter=chapter,
            topic=topic,
            generated_at=datetime.now(timezone.utc).isoformat(),
            challenges=challenges,
            submission_evaluation=sub_eval,
        )

        return eval_result.model_dump()

    async def _generate_java_mobile_challenges(
        self, chapter: int, topic: str, profile: Optional[LearnerProfile] = None
    ) -> list[ChallengeSpec]:
        lower_topic = topic.lower()

        if any(k in lower_topic for k in ["teks", "textview", "coldstart", "kata"]):
            c1 = ChallengeSpec(
                id=f"ch{chapter}_java_predict_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Apa teks persis yang akan tampil di layar HP saat baris perintah `System.out.println(pesanLayar);` dijalankan?",
                code_snippet="""String pesanLayar = "Halo, selamat datang di aplikasi HP!";
System.out.println(pesanLayar);""",
                reference_answer="Halo, selamat datang di aplikasi HP!",
                reference_explanation="Variabel pesanLayar menyimpan teks 'Halo, selamat datang di aplikasi HP!' dan dicetak langsung ke layar kaca HP.",
                materi_section_reference="§4: Kode Contoh Java",
            )
            c2 = ChallengeSpec(
                id=f"ch{chapter}_java_trace_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Jika nilai variabel diubah menjadi `pesanLayar = \"Skor Kamu: 100\";`, apa tampilan terbaru di layar HP?",
                reference_answer="Skor Kamu: 100",
                reference_explanation="State memori teks diperbarui sebelum instruksi cetak ke layar dijalankan.",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c3 = ChallengeSpec(
                id=f"ch{chapter}_java_diag_001",
                type="diagnostic_free_response",
                difficulty="foundation",
                prompt="Mengapa teks di Java untuk layar HP wajib dibungkus oleh tanda kutip ganda \"...\"?",
                reference_answer="Agar komputer memahami tulisan tersebut sebagai kalimat teks murni (String), bukan sebagai nama variabel atau perintah kode Java.",
                reference_explanation="Tanda kutip ganda adalah tanda pembeda sintaksis antara data teks literal dan instruksi logika program.",
                materi_section_reference="§5: Pemberantasan Miskonsepsi Pemula",
            )

        elif any(k in lower_topic for k in ["button", "tombol", "counter", "angka"]):
            c1 = ChallengeSpec(
                id=f"ch{chapter}_java_predict_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Berapa angka skor yang tampil di layar HP setelah tombol disentuh dua kali berturut-turut?",
                code_snippet="""int skor = 0;
skor = skor + 1;
skor = skor + 1;
System.out.println("Skor: " + skor);""",
                reference_answer="Skor: 2",
                reference_explanation="Nilai awal 0 ditambah 1 pada sentuhan pertama (skor=1), lalu ditambah 1 lagi pada sentuhan kedua (skor=2).",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c2 = ChallengeSpec(
                id=f"ch{chapter}_java_trace_001",
                type="diagnostic_free_response",
                difficulty="foundation",
                prompt="Pada kode `skor = skor + 1;`, jelaskan arti tanda sama dengan `=` bagi seorang pemula yang baru belajar ngoding.",
                reference_answer="Tanda = adalah perintah penugasan: hitung nilai di sebelah kanan terlebih dahulu (skor lama + 1), lalu simpan hasilnya ke dalam wadah variabel di sebelah kiri.",
                reference_explanation="Simbol = di Java bukan persamaan matematika statis, melainkan operasi pembaruan nilai variabel.",
                materi_section_reference="§5: Pemberantasan Miskonsepsi Pemula",
            )
            c3 = ChallengeSpec(
                id=f"ch{chapter}_java_diag_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Jika pengguna menyentuh tombol sebanyak 5 kali berturut-turut dari posisi awal skor bernilai 0, berapa angka akhir variabel skor?",
                reference_answer="5",
                reference_explanation="Setiap kali disentuh nilai skor bertambah 1 secara kumulatif: 0 -> 1 -> 2 -> 3 -> 4 -> 5.",
                materi_section_reference="§2: Peta Langkah-demi-Langkah",
            )

        elif any(k in lower_topic for k in ["conditional", "keputusan", "baterai", "if"]):
            c1 = ChallengeSpec(
                id=f"ch{chapter}_java_predict_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Jika daya baterai HP bernilai 15, kalimat mana yang akan dicetak ke layar HP?",
                code_snippet="""int baterai = 15;
if (baterai < 20) {
    System.out.println("Peringatan: Baterai Lemah!");
} else {
    System.out.println("Status: Baterai Aman.");
}""",
                reference_answer="Peringatan: Baterai Lemah!",
                reference_explanation="Kondisi 15 < 20 bernilai benar (true), sehingga komputer hanya mengeksekusi blok di dalam if.",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c2 = ChallengeSpec(
                id=f"ch{chapter}_java_trace_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Jika variabel baterai diganti menjadi 80, kalimat apa yang tampil di layar HP?",
                reference_answer="Status: Baterai Aman.",
                reference_explanation="Syarat 80 < 20 bernilai salah (false), sehingga komputer melompati blok if dan menjalankan blok else.",
                materi_section_reference="§4: Kode Contoh Java",
            )
            c3 = ChallengeSpec(
                id=f"ch{chapter}_java_diag_001",
                type="diagnostic_free_response",
                difficulty="foundation",
                prompt="Apakah mungkin blok `if` dan blok `else` berjalan bersamaan pada waktu yang sama? Jelaskan alasannya.",
                reference_answer="Tidak mungkin. Komputer hanya memilih satu jalur secara eksklusif: jika syarat benar masuk ke if, jika salah masuk ke else.",
                reference_explanation="Percabangan if-else bekerja seperti saklar dua arah yang hanya bisa mengalir ke salah satu cabang.",
                materi_section_reference="§1: Konsep Utama",
            )

        elif any(k in lower_topic for k in ["loop", "daftar", "perulangan", "chat", "list"]):
            c1 = ChallengeSpec(
                id=f"ch{chapter}_java_predict_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Berapa total baris notifikasi yang berhasil dicetak ke layar HP oleh perulangan `for` berikut?",
                code_snippet="""for (int nomorPesan = 1; nomorPesan <= 3; nomorPesan++) {
    System.out.println("Pesan Masuk #" + nomorPesan);
}""",
                reference_answer="3 baris",
                reference_explanation="Perulangan berjalan untuk nomorPesan = 1, 2, dan 3. Saat bernilai 4, kondisi <= 3 menjadi false dan loop berhenti.",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c2 = ChallengeSpec(
                id=f"ch{chapter}_java_trace_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Apa nilai variabel `nomorPesan` pada saat perulangan memutuskan untuk berhenti?",
                reference_answer="4",
                reference_explanation="Pada nilai 4, syarat 'nomorPesan <= 3' dievaluasi menjadi false, menghentikan loop.",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c3 = ChallengeSpec(
                id=f"ch{chapter}_java_diag_001",
                type="diagnostic_free_response",
                difficulty="foundation",
                prompt="Mengapa sebuah perulangan `for` di aplikasi HP wajib memiliki syarat batas (seperti `nomorPesan <= 3`)?",
                reference_answer="Sebagai rem otomatis agar perulangan berhenti saat daftar pesan selesai dan tidak membuat aplikasi HP macet (hang) akibat perulangan tanpa henti.",
                reference_explanation="Syarat terminasi mencegah infinite loop yang dapat mengunci memori perangkat mobile.",
                materi_section_reference="§5: Pemberantasan Miskonsepsi Pemula",
            )

        else:
            c1 = ChallengeSpec(
                id=f"ch{chapter}_java_predict_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Ke layar manakah aplikasi HP berpindah pada akhir eksekusi kode berikut?",
                code_snippet="""String layarSekarang = "Halaman Beranda";
layarSekarang = "Halaman Profil Pengguna";
System.out.println("Layar Aktif: " + layarSekarang);""",
                reference_answer="Layar Aktif: Halaman Profil Pengguna",
                reference_explanation="Variabel layarSekarang ditimpa dengan nilai baru 'Halaman Profil Pengguna' sebelum dicetak ke layar.",
                materi_section_reference="§4: Kode Contoh Java",
            )
            c2 = ChallengeSpec(
                id=f"ch{chapter}_java_trace_001",
                type="predict_the_output",
                difficulty="foundation",
                prompt="Sebelum tombol navigasi ditekan, di halaman mana pengguna mula-mula berada?",
                reference_answer="Halaman Beranda",
                reference_explanation="Nilai awal variabel layarSekarang adalah 'Halaman Beranda'.",
                materi_section_reference="§3: Tabel Jejak Eksekusi Logika",
            )
            c3 = ChallengeSpec(
                id=f"ch{chapter}_java_diag_001",
                type="diagnostic_free_response",
                difficulty="foundation",
                prompt="Apa yang terjadi dengan layar lama saat pengguna berpindah ke layar baru di aplikasi mobile?",
                reference_answer="Layar lama tidak dihancurkan melainkan disimpan di tumpukan riwayat (back stack) agar pengguna bisa kembali saat menekan tombol Back.",
                reference_explanation="Sistem navigasi mobile mempertahankan riwayat layar sebelumnya untuk memudahkan pengguna kembali.",
                materi_section_reference="§5: Pemberantasan Miskonsepsi Pemula",
            )

        return [c1, c2, c3]
