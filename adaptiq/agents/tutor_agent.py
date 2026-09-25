"""Tutor Agent for generating adaptive learning materials (materi.md)."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field

from adaptiq.state.learner_profile import LearnerProfile
from adaptiq.tools.code_validator import CodeValidator

FORBIDDEN_APHANTASIA_WORDS = [
    "imagine",
    "visualize",
    "picture",
    "think of",
    "bayangkan",
    "visualisasikan",
    "pikirkan di benak",
    "bayangkan di benak",
    "dalam benakmu",
]


class TutorAgentInput(BaseModel):
    session_id: str
    topic: str
    chapter_number: int = 1
    prerequisites: list[str] = Field(default_factory=list)
    learner_profile: LearnerProfile
    previous_misconceptions: list[str] = Field(default_factory=list)
    remediation_mode: bool = False


class TutorAgent:
    """Pedagogical Tutor Agent responsible for generating materi.md."""

    def __init__(
        self,
        prompt_template_path: Optional[str] = None,
        api_key: Optional[str] = None,
        code_validator: Optional[CodeValidator] = None,
    ):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.template_path = Path(
            prompt_template_path
            or Path(__file__).parent.parent / "prompts" / "tutor_system_prompt.txt"
        )
        self.validator = code_validator or CodeValidator()

    def determine_modality(self, visual_imagery_score: float) -> str:
        if visual_imagery_score <= 3.0:
            return "aphantasia_adapted"
        elif visual_imagery_score >= 8.0:
            return "hyper_visual"
        return "standard"

    def filter_forbidden_words(self, text: str) -> str:
        """Strip forbidden imagery words for Aphantasia-adapted mode."""
        cleaned = text
        for word in FORBIDDEN_APHANTASIA_WORDS:
            cleaned = re.sub(re.escape(word), "[formal concept]", cleaned, flags=re.IGNORECASE)
        return cleaned

    def check_forbidden_words(self, text: str) -> list[str]:
        """Return list of forbidden words present in text."""
        lower = text.lower()
        return [word for word in FORBIDDEN_APHANTASIA_WORDS if word.lower() in lower]

    async def generate_material(self, agent_input: TutorAgentInput) -> str:
        score = agent_input.learner_profile.cognitive_traits.visual_imagery_score
        modality = self.determine_modality(score)

        # Attempt live LLM call if api_key is configured
        if self.api_key and not self.api_key.startswith("your_"):
            try:
                from google import genai

                client = genai.Client(api_key=self.api_key)
                prompt_template = self.template_path.read_text(encoding="utf-8")

                system_prompt = (
                    prompt_template.replace("{{session_id}}", agent_input.session_id)
                    .replace("{{topic}}", agent_input.topic)
                    .replace("{{chapter_number}}", str(agent_input.chapter_number))
                    .replace("{{remediation_mode}}", str(agent_input.remediation_mode).lower())
                    .replace("{{prerequisites}}", json.dumps(agent_input.prerequisites))
                    .replace(
                        "{{learner_profile_json}}",
                        json.dumps(agent_input.learner_profile.model_dump(), indent=2),
                    )
                    .replace(
                        "{{previous_misconceptions_array}}",
                        json.dumps(agent_input.previous_misconceptions),
                    )
                )

                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents="Generate materi.md according to system instructions.",
                    config={
                        "system_instruction": system_prompt,
                        "temperature": 0.7,
                        "max_output_tokens": 4096,
                    },
                )
                if response.text and response.text.strip():
                    content = response.text.strip()
                    if modality == "aphantasia_adapted":
                        content = self.filter_forbidden_words(content)
                    return content
            except Exception as e:
                # Log and fallback to offline generator
                print(f"[TutorAgent] Warning: LLM generation error ({e}), falling back to deterministic template.")

        # High-fidelity deterministic fallback matching PRD Section 3.1
        content = self._generate_fallback_material(agent_input, modality, score)
        if modality == "aphantasia_adapted":
            # Extra guardrail against accidental forbidden words
            content = self.filter_forbidden_words(content)

        return content

    def _is_java_topic(self, topic: str) -> bool:
        lower = topic.lower()
        if "javascript" in lower or "js " in lower or lower.endswith("js"):
            return False
        return any(k in lower for k in ["java", "mobile", "android", "layar", "tombol", "intent", "counter", "textview", "notifikasi"])

    def _generate_fallback_material(
        self, agent_input: TutorAgentInput, modality: str, score: float
    ) -> str:
        if self._is_java_topic(agent_input.topic):
            return self._generate_java_mobile_material(agent_input, modality, score)

        now_iso = datetime.now(timezone.utc).isoformat()
        is_aphantasia = modality == "aphantasia_adapted"

        if is_aphantasia:
            mechanism_section = """## 2. Core Mechanism (State Machine & Trace)

The runtime maintains five distinct operational phases:
1. `EXEC_STACK`: Synchronous frame evaluation
2. `CHECK_MICROTASK`: Evaluates and empties microtask queue
3. `RENDER_CHECK`: Browser paint opportunity
4. `DEQUEUE_MACROTASK`: Shift single macrotask into execution stack
5. `LOOP_RECYCLE`: Return to Step 1

```
State Transition Table:
[RUNNING] ---> [STACK_EMPTY] ---> [DRAIN_MICROTASK] ---> [DRAIN_MACROTASK] ---> [IDLE]
```"""
            trace_section = """## 4. Execution Trace Table (Aphantasia-Adapted)

| Step | Call Stack State     | Web API Queue   | Microtask Queue | Macrotask Queue | Console Output |
|------|----------------------|-----------------|-----------------|-----------------|----------------|
| 1    | [main()]             | -               | -               | -               | -              |
| 2    | [main(), log('A')]   | -               | -               | -               | A              |
| 3    | [main(), setTimeout] | timer(cb1, 0ms) | -               | -               | -              |
| 4    | [main(), Promise]    | -               | [cb_micro]      | -               | -              |
| 5    | [main(), log('D')]   | -               | [cb_micro]      | [cb_macro]      | D              |
| 6    | [EMPTY]              | -               | []              | [cb_macro]      | C              |
| 7    | [cb_macro]           | -               | []              | []              | B              |"""
        else:
            mechanism_section = """## 2. Core Mechanism

The Event Loop continuously coordinates synchronous execution with background task queues.

**Analogy:** Think of the runtime like a single chef (Call Stack) preparing meals. When an order takes time to bake (setTimeout/fetch), the chef places it in an oven (Web API) and continues with the next immediate dish. When the timer rings, the ready dish is moved to a serving counter (Queue) until the chef's hands are free."""
            trace_section = """## 4. Execution Trace Table

| Step | Call Stack State     | Web API Queue   | Microtask Queue | Macrotask Queue | Console Output |
|------|----------------------|-----------------|-----------------|-----------------|----------------|
| 1    | [main()]             | -               | -               | -               | -              |
| 2    | [main(), log('A')]   | -               | -               | -               | A              |
| 3    | [main(), setTimeout] | timer(cb1, 0ms) | -               | -               | -              |
| 4    | [main(), log('D')]   | -               | -               | [cb_macro]      | D              |
| 5    | [cb_macro]           | -               | -               | []              | B              |"""

        # Frontmatter must match strict YAML format
        return f"""---
artifact_type: "materi"
session_id: "{agent_input.session_id}"
topic: "{agent_input.topic}"
chapter: {agent_input.chapter_number}
estimated_reading_time_minutes: 10
prerequisites: {json.dumps(agent_input.prerequisites)}
cognitive_profile_applied: "{modality}"
visual_imagery_score_at_generation: {score}
remediation_mode: {str(agent_input.remediation_mode).lower()}
chapter_overflow: false
generated_at: "{now_iso}"
misconceptions_targeted: {json.dumps(agent_input.previous_misconceptions)}
---

# Chapter {agent_input.chapter_number}: {agent_input.topic}

## 1. Formal Definition
The JavaScript Event Loop is a single-threaded concurrent execution coordinator that processes frames sequentially from the Call Stack and enqueues asynchronous callbacks across microtask and macrotask FIFO queues.

{mechanism_section}

## 3. Annotated Code Specimen
```javascript
console.log('A');           // STACK: [main]            -> PRINT: A
setTimeout(() => {{
  console.log('B');         // MACROTASK: executed after microtask drain
}}, 0);
Promise.resolve().then(() => {{
  console.log('C');         // MICROTASK: priority queue drained immediately after stack
}});
console.log('D');           // STACK: [main]            -> PRINT: D
```

{trace_section}

## 5. Misconception Inoculation
- **Misconception:** `setTimeout(fn, 0)` executes synchronously or immediately on the next line.
- **Correction:** `setTimeout` delegates to host timers (Web API / libuv). Its callback enters the Macrotask Queue and runs only after the Call Stack and Microtask Queue are completely clear.

## 6. Concept Check (Pre-Assessment Primer)
1. Which queue has absolute priority when the Call Stack becomes empty: Microtasks or Macrotasks?
2. What is the output order of lines A, B, C, and D in Section 3?
"""

    def _generate_java_mobile_material(
        self, agent_input: TutorAgentInput, modality: str, score: float
    ) -> str:
        now_iso = datetime.now(timezone.utc).isoformat()
        lower_topic = agent_input.topic.lower()

        if any(k in lower_topic for k in ["teks", "textview", "coldstart", "kata"]):
            title = "Layar HP & Menampilkan Teks Pertama (TextView)"
            analogy = (
                "Layar aplikasi HP bekerja seperti papan nama digital di depan toko.\n\n"
                "Untuk memunculkan teks, kita menyiapkan wadah tulisan (variabel `String`) yang berisi kalimat, "
                "lalu memerintahkan sistem HP untuk menampilkan isi wadah tersebut ke layar kaca HP."
            )
            steps = (
                "1. **Siapkan Wadah Program**: Menulis class pembungkus aplikasi HP.\n"
                "2. **Buat Wadah Kalimat**: Menyiapkan variabel teks `String pesan = \"...\";`.\n"
                "3. **Tampilkan ke Layar**: Mengirim perintah kerja `System.out.println` untuk mencetak ke layar."
            )
            trace_table = (
                "| Step | Baris Kode | State Memori HP | Efek Tampilan Layar HP |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| 1 | `String pesan = \"Halo Mobile!\";` | Variabel `pesan` berisi text | Layar HP masih kosong |\n"
                "| 2 | `System.out.println(pesan);` | State memori tetap stabil | Layar memunculkan: Halo Mobile! |"
            )
            code_snippet = """```java
public class DemoTextViewApp {
    public static void main(String[] args) {
        // 1. Simpan kalimat yang ingin dimunculkan di layar HP
        String pesanLayar = "Halo, selamat datang di aplikasi HP pertamaku!";
        
        // 2. Perintahkan sistem HP untuk mencetak pesan ke layar
        System.out.println(pesanLayar);
    }
}
```"""
            misconception = (
                "- **Miskonsepsi Pemula:** Mengira teks bisa ditulis langsung tanpa tanda kutip dua.\n"
                "- **Koreksi Nyata:** Di Java, semua teks wajib diapit tanda kutip ganda `\"...\"` agar komputer mengenalnya sebagai kalimat, bukan perintah kode."
            )
            quiz = (
                "- **Pertanyaan:** Apa yang akan tampil di layar HP jika nilai `pesanLayar` diubah menjadi `\"Skor: 100\"`?\n"
                "- **Aksi:** Tuliskan kalimat persis yang muncul pada layar HP."
            )

        elif any(k in lower_topic for k in ["button", "tombol", "counter", "angka"]):
            title = "Tombol Interaktif & Variabel Angka (Button & Counter)"
            analogy = (
                "Tombol di aplikasi HP bekerja persis seperti saklar bel pintu otomatis.\n\n"
                "Setiap kali jari pengguna menyentuh tombol, saklar terpicu untuk menambah angka counter pada papan skor digital."
            )
            steps = (
                "1. **Atur Angka Awal**: Menyiapkan variabel angka bulat `int skor = 0;`.\n"
                "2. **Sentuhan Pertama**: Tombol disentuh, lakukan penambahan `skor = skor + 1;`.\n"
                "3. **Perbarui Layar**: Tampilkan angka skor terbaru ke layar HP agar pengguna melihat perubahan."
            )
            trace_table = (
                "| Step | Aksi / Baris Kode | State Variabel `skor` | Teks Tampil di Layar HP |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| 1 | `int skor = 0;` | `skor = 0` | Layar: Skor = 0 |\n"
                "| 2 | Sentuh Tombol 1 (`skor = skor + 1;`) | `skor = 1` | Layar: Skor = 1 |\n"
                "| 3 | Sentuh Tombol 2 (`skor = skor + 1;`) | `skor = 2` | Layar: Skor = 2 |"
            )
            code_snippet = """```java
public class DemoButtonApp {
    public static void main(String[] args) {
        // 1. Siapkan angka skor awal bernilai 0
        int skor = 0;
        System.out.println("Layar Awal: Skor = " + skor);
        
        // 2. Simulasikan sentuhan tombol pertama
        skor = skor + 1;
        System.out.println("Klik 1: Skor = " + skor);
        
        // 3. Simulasikan sentuhan tombol kedua
        skor = skor + 1;
        System.out.println("Klik 2: Skor = " + skor);
    }
}
```"""
            misconception = (
                "- **Miskonsepsi Pemula:** Mengira `skor = skor + 1` adalah persamaan matematika mustahil.\n"
                "- **Koreksi Nyata:** Simbol `=` di Java adalah penugasan (assignment), artinya hitung angka di kanan lalu masukkan hasilnya ke wadah variabel di kiri."
            )
            quiz = (
                "- **Pertanyaan:** Jika tombol disentuh 3 kali lagi berturut-turut, berapa angka akhir pada variabel `skor`?\n"
                "- **Aksi:** Hitung langkah demi langkah menggunakan tabel state."
            )

        elif any(k in lower_topic for k in ["conditional", "keputusan", "baterai", "if"]):
            title = "Logika Keputusan di Layar HP (if-else & State)"
            analogy = (
                "Logika keputusan di HP bekerja seperti saklar sensor lampu otomatis.\n\n"
                "Jika daya baterai HP di bawah 20 persen, sensor menyalakan tanda peringatan merah. Jika tidak, tanda aman hijau yang menyala."
            )
            steps = (
                "1. **Cek Nilai Sensor**: Memeriksa angka daya baterai HP (`int baterai = 15;`).\n"
                "2. **Evaluasi Syarat**: Memeriksa apakah `baterai < 20` bernilai benar (`true`) atau salah (`false`).\n"
                "3. **Pilih Jalur Eksekusi**: Menampilkan peringatan baterai lemah hanya jika syarat terpenuhi."
            )
            trace_table = (
                "| Step | Baris Kode | Evaluasi Logika | Jalur Layar yang Muncul |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| 1 | `int baterai = 15;` | `baterai = 15` | Memori mencatat angka daya 15 |\n"
                "| 2 | `if (baterai < 20)` | `15 < 20` -> `true` | Memilih blok IF (Baterai Lemah!) |\n"
                "| 3 | `System.out.println(...)` | Eksekusi cetak teks | Layar: Peringatan Baterai Lemah! |"
            )
            code_snippet = """```java
public class DemoStatusApp {
    public static void main(String[] args) {
        // 1. Nilai daya baterai HP saat ini
        int baterai = 15;
        
        // 2. Evaluasi kondisi dan ambil keputusan tampilan
        if (baterai < 20) {
            System.out.println("Status Layar: Baterai Lemah, Segera Cas HP!");
        } else {
            System.out.println("Status Layar: Baterai Aman dan Normal.");
        }
    }
}
```"""
            misconception = (
                "- **Miskonsepsi Pemula:** Mengira kedua blok `if` dan `else` bisa berjalan bersamaan.\n"
                "- **Koreksi Nyata:** Komputer hanya memilih satu jalur saja secara eksklusif tergantung kondisi benar atau salah."
            )
            quiz = (
                "- **Pertanyaan:** Jika nilai `baterai` diubah menjadi 80, teks mana yang akan tercetak di layar HP?\n"
                "- **Aksi:** Tuliskan pilihan teks yang dieksekusi."
            )

        elif any(k in lower_topic for k in ["loop", "daftar", "perulangan", "chat", "list"]):
            title = "Menampilkan Daftar Berulang di Layar HP (for Loop)"
            analogy = (
                "Perulangan di HP bekerja seperti mesin pencetak tiket nomor antrean otomatis.\n\n"
                "Mesin mencetak baris pesan satu per satu secara berurutan sampai jumlah target yang ditentukan tercapai."
            )
            steps = (
                "1. **Tentukan Nomor Awal**: Mulai dari nomor urut 1 (`int i = 1;`).\n"
                "2. **Tentukan Batas Akhir**: Berhenti setelah mencapai batas maksimal (`i <= 3;`).\n"
                "3. **Langkah Inkremental**: Naikkan nomor urut satu per satu (`i++`) setiap baris tercetak."
            )
            trace_table = (
                "| Iterasi | Nilai `i` | Cek Syarat `i <= 3` | Baris Teks yang Tercetak di Layar HP |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| 1 | `1` | `true` | Pesan Masuk #1: Halo dari aplikasi! |\n"
                "| 2 | `2` | `true` | Pesan Masuk #2: Halo dari aplikasi! |\n"
                "| 3 | `3` | `true` | Pesan Masuk #3: Halo dari aplikasi! |\n"
                "| 4 | `4` | `false` | Loop berhenti otomatis |"
            )
            code_snippet = """```java
public class DemoLoopApp {
    public static void main(String[] args) {
        // Cetak 3 baris notifikasi pesan di aplikasi mobile
        for (int nomorPesan = 1; nomorPesan <= 3; nomorPesan++) {
            System.out.println("Pesan Masuk #" + nomorPesan + ": Ada update terbaru!");
        }
        System.out.println("Semua daftar pesan telah tampil di layar.");
    }
}
```"""
            misconception = (
                "- **Miskonsepsi Pemula:** Mengira perulangan `for` akan berjalan selamanya tanpa henti.\n"
                "- **Koreksi Nyata:** Perulangan memiliki rem otomatis (syarat terminasi). Saat syarat bernilai `false`, perulangan langsung berhenti."
            )
            quiz = (
                "- **Pertanyaan:** Berapa kali teks pesan akan tercetak jika syarat perulangan diganti menjadi `nomorPesan <= 5`?\n"
                "- **Aksi:** Sebutkan total baris pesan yang dihasilkan."
            )

        else:
            title = "Pindah Layar Aplikasi HP (Intent & Navigasi)"
            analogy = (
                "Pindah layar di HP bekerja persis seperti membuka pintu penghubung antara dua ruangan.\n\n"
                "Pengguna berjalan dari Ruang Tamu (Layar Utama) menuju Ruang Makan (Layar Profil) sambil membawa data yang diperlukan."
            )
            steps = (
                "1. **Cek Layar Aktif**: Mengetahui posisi layar pengguna saat ini (`String layarAktif`).\n"
                "2. **Picu Navigasi**: Pengguna menyentuh tombol menuju layar tujuan.\n"
                "3. **Ganti Tampilan Layar**: Sistem HP mengalihkan tampilan ke layar baru secara mulus."
            )
            trace_table = (
                "| Step | Baris Kode / Aksi | Layar Aktif HP | Keterangan |\n"
                "| :--- | :--- | :--- | :--- |\n"
                "| 1 | `String layar = \"Beranda\";` | Layar Beranda | Pengguna melihat menu utama |\n"
                "| 2 | Klik tombol navigasi | Transisi Navigasi | Sistem menyiapkan layar profil |\n"
                "| 3 | `layar = \"Halaman Profil\";` | Halaman Profil | Pengguna telah tiba di layar profil |"
            )
            code_snippet = """```java
public class DemoNavigasiApp {
    public static void main(String[] args) {
        // 1. Posisi layar awal pengguna
        String layarSekarang = "Halaman Beranda Aplikasi";
        System.out.println("Layar Sekarang: " + layarSekarang);
        
        // 2. Simulasi pengguna menekan tombol profil
        System.out.println("Aksi: Pengguna menekan tombol Buka Profil");
        
        // 3. Pindahkan layar ke halaman profil
        layarSekarang = "Halaman Profil Pengguna";
        System.out.println("Layar Sekarang Berpindah Ke: " + layarSekarang);
    }
}
```"""
            misconception = (
                "- **Miskonsepsi Pemula:** Mengira layar lama langsung hancur seketika tanpa jejak.\n"
                "- **Koreksi Nyata:** Di HP, layar lama disimpan dalam tumpukan riwayat (back stack) sehingga pengguna bisa menekan tombol Back untuk kembali."
            )
            quiz = (
                "- **Pertanyaan:** Ke layar manakah aplikasi berpindah pada akhir eksekusi kode di atas?\n"
                "- **Aksi:** Tuliskan nama layar tujuan akhir."
            )

        return f"""---
artifact_type: "materi"
session_id: "{agent_input.session_id}"
topic: "{agent_input.topic}"
chapter: {agent_input.chapter_number}
estimated_reading_time_minutes: 8
prerequisites: {json.dumps(agent_input.prerequisites)}
cognitive_profile_applied: "{modality}"
visual_imagery_score_at_generation: {score}
remediation_mode: {str(agent_input.remediation_mode).lower()}
chapter_overflow: false
generated_at: "{now_iso}"
misconceptions_targeted: {json.dumps(agent_input.previous_misconceptions)}
---

# 📱 Bab {agent_input.chapter_number}: {title}

## 💡 1. Konsep Utama (Analogi Mekanis Dunia Nyata)
{analogy}

## 📋 2. Peta Langkah-demi-Langkah (Dyslexia-Friendly)
{steps}

## 📊 3. Tabel Jejak Eksekusi Logika & State Memori HP (Aphantasia-Friendly)
{trace_table}

## 💻 4. Kode Contoh Java (Siap Jalan di JDK 21+)
{code_snippet}

## 🛡️ 5. Pemberantasan Miskonsepsi Pemula
{misconception}

## 🧩 6. Kuis Mini Interaktif
{quiz}
"""
