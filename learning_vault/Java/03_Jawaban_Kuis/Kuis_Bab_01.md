# 📝 Jawaban Kuis — Bab 1: Pengenalan Java

> Tulis jawabanmu di bawah ini, lalu kabari tutormu untuk dikoreksi!

---

## Soal 1 — Pilihan Ganda
**Jawabanku**: B

**Alasanku**: karena pada saat mempelajari struktur java ada beberapa hal yang saya catat dimana bagian yang paling atas adalah membuat class, membuat pintu main, keterakhir isi dari ruangan main nya 

---

## Soal 2 — Jejak Eksekusi

| Step | Baris yang Dieksekusi            | Output di Konsol |     |
| :--- | :------------------------------- | :--------------- | --- |
| 1    | `System.out.println("Satu");`    | Satu             |     |
| 2    | `System.out.print("Dua ");`      | Dua              |     |
| 3    | `System.out.print("Tiga");`      | Dua Tiga         |     |
| 4    | `System.out.println("!");`       | !                |     |
| 5    | `System.out.println("Selesai");` | Selesai          |     |

**Jawaban bonus** (total baris teks): 5

---

## Soal 3 — Temukan Bug

**Kesalahan 1**: public class buggy

**Kesalahan 2**: System.out.println("Program mulai")

**Kode yang sudah diperbaiki**:
```java
public class Buggy {
    public static void main(String[] args) {
        System.out.println("Program mulai");
        System.out.println("Program selesai");
    }
}
```

---

## Catatan / Pertanyaan Tambahanku:
*(Tulis jika ada yang masih membingungkan — pertanyaan apapun itu bagus!)*
