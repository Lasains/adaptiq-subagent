---
artifact_type: "materi"
topic: "Java Mobile - Layar HP & Menampilkan Teks Pertama (TextView & String)"
chapter: 1
estimated_reading_time_minutes: 8
cognitive_profile_applied: "aphantasia_adapted"
visual_imagery_score_at_generation: 1.0
dyslexia_mode: true
---

# 📱 Bab 1: Layar HP & Menampilkan Teks Pertama (TextView)

## 💡 1. Konsep Utama (Analogi Dunia Nyata)
Layar aplikasi HP bekerja seperti **papan nama digital di depan toko**.

Untuk memunculkan tulisan di layar HP, kita menyiapkan wadah tulisan (variabel `String`) yang berisi kalimat, lalu memerintahkan sistem HP untuk mencetak isi wadah tersebut ke layar kaca HP.

---

## 📋 2. Peta Langkah-demi-Langkah (Dyslexia-Friendly)
1. **Siapkan Wadah Program**: Menulis class pembungkus program aplikasi HP.
2. **Buat Wadah Kalimat**: Menyiapkan variabel teks `String pesan = "...";`.
3. **Tampilkan ke Layar**: Mengirim perintah kerja `System.out.println(pesan)` untuk mencetak ke layar.

---

## 📊 3. Tabel Jejak Eksekusi Logika & State Memori HP (Aphantasia-Friendly)

| Step | Baris Kode | State Memori HP | Efek Tampilan Layar HP |
| :--- | :--- | :--- | :--- |
| **1** | `String pesan = "Halo Mobile!";` | Variabel `pesan` menyimpan teks | Layar HP masih kosong |
| **2** | `System.out.println(pesan);` | State memori tetap stabil | Layar memunculkan tulisan: **Halo Mobile!** |

---

## 💻 4. Kode Contoh Java (Siap Jalan di JDK 21+)

```java
public class DemoTextViewApp {
    public static void main(String[] args) {
        // 1. Simpan kalimat yang ingin dimunculkan di layar HP
        String pesanLayar = "Halo, selamat datang di aplikasi HP pertamaku!";
        
        // 2. Perintahkan sistem HP untuk mencetak pesan ke layar
        System.out.println(pesanLayar);
    }
}
```

---

## 🛡️ 5. Pemberantasan Miskonsepsi Pemula
- **Miskonsepsi:** Mengira teks di Java bisa ditulis langsung tanpa tanda kutip dua.
- **Koreksi Nyata:** Di Java, semua teks wajib diapit tanda kutip ganda `"`...`"` agar komputer memahaminya sebagai kalimat teks (String), bukan sebagai nama perintah kode.

---

## 🧩 6. Kuis Interaktif Bab 1
Coba jawab 2 pertanyaan ini (bisa kamu jawab di folder `03_Jawaban_Kuis/Jawaban_Bab_01.md`):

1. **Soal Tebak Tampilan Layar**:  
   Jika nilai variabel diubah menjadi:
   ```java
   String pesanLayar = "Skor Kamu: 100";
   System.out.println(pesanLayar);
   ```
   Teks persis apa yang akan muncul di layar kaca HP?

2. **Soal Konsep**:  
   Mengapa teks `"Halo Mobile!"` wajib diapit oleh tanda kutip dua? Apa yang terjadi jika tanda kutip itu dihapus?
