# 📝 Jawaban Kuis — Bab 4: Percabangan

> Tulis jawabanmu di bawah ini, lalu kabari tutormu untuk dikoreksi!

---

## Soal 1 — Pilihan Ganda
**Jawabanku**: C. Cukup

**Alasanku**: Dikarenakan syarat dari cabang yang ke dua bisa di penuhi oleh angka 75 dimana java ketika sudah menemukan cabang yang  bisa memenuhi syaratnya maka java tidak memeriksa lagi di bawahnya

---

## Soal 2 — Jejak Eksekusi `switch`

| Step | Yang Dicek | Cocok? | Yang Terjadi                                                        |
| :--- | :--------- | :----: | :------------------------------------------------------------------ |
| 1    | `case 1:`  | tidak  | isi perintah tidak di jalankan dan memeriksa cabang/case berikutnya |
| 2    | `case 2:`  |  iya   | isi perintah di jalankan dan kan berhenti di sini                   |
| 3    | `case 3:`  | tidak  | case tidak di cek karena case sebelumnya sudah cocok                |

**Output akhir program**: *(tulis jawabanmu)*

---

## Soal 3 — Temukan Bug

**Kesalahan 1**: if (umur >= 13) { System.out.println("Remaja atau dewasa");} 

**Kesalahan 2**: else if (umur >= 18) { System.out.println("Dewasa"); }

**Kode yang sudah diperbaiki**:
```java
public class CekUmur {
    public static void main(String[] args) {
        int umur = 20;

        if (umur >= 18) {
            System.out.println("Dewasa");
        } else if (umur >= 13) {
            System.out.println("Remaja");
        } else {
            System.out.println("Anak-anak");
        }
    }
}
```

---

## Soal 4 — Coding Mini

```java
public class kategoriIMT{
	public static void main(String[] args){
		double imt = 22.5;
		
		if (imt < 18.5){
			System.out.println("IMT Kamu: " + imt);
			System.out.println("Kategori: Kurus");
		} else if (imt >= 18.5 || imt < 25){
			System.out.prinln("IMT Kamu: " + imt);
			System.out.println("Kategori: Normal");
		} else if (imt >= 25 || imt < 30){
			System.out.println("IMT Kamu: " + imt);
			System.out.println("Kategori: Gemuk");
		} else {
			System.out.println("IMT Kamu: " + imt);
			System.out.println("Kategori: Obesitas");
		}
	}
}
```

---

## Catatan / Pertanyaan Tambahanku:
*(Tulis jika ada yang masih membingungkan)*
