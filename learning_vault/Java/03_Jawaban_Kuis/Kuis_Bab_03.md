# 📝 Jawaban Kuis — Bab 3: Operator

> Tulis jawabanmu di bawah ini, lalu kabari tutormu untuk dikoreksi!

---

## Soal 1 — Pilihan Ganda
**Jawabanku**: A

**Alasanku**: karena int akan menghiraukan angka desimal yang ada jadi semisal angka 10.5 di int yang terbaca hanya 10

---

## Soal 2 — Jejak Eksekusi


| Step | Operasi            | Nilai `skor` Setelahnya |
| :--- | :----------------- | :---------------------- |
| 1    | `int skor = 50;`   | 50                      |
| 2    | `skor += 30;`      | 80                      |
| 3    | `skor *= 2;`       | 160                     |
| 4    | `skor -= 20;`      | 140                     |
| 5    | `skor++;`          | 141                     |
| 6    | `println` mencetak | 141                     |

---

## Soal 3 — Prediksi Output Logika

| Ekspresi            | Prediksi (`true` / `false`) |
| :------------------ | :-------------------------- |
| `a == c`            | true                        |
| `a != b`            | true                        |
| `a > b && b > 0`    | true                        |
| `a < b \|\| c == 8` | true                        |
| `!(a == b)`         | true                        |
| `a >= c && b <= 2`  | true                        |

---

## Soal 4 — Coding Mini

```java
public class CekKelayakan{
	public static void main(String[] args){
		int umur = 17;
		boolean punyaKtp = false;
		
		System.out.println("Umur: " + umur);
		System.out.println("Punya KTP: " + punyaKtp);
		System.out.println("Layak Memilih: " + (umur >= 17 && punyaKtp == true));
	}
}
```

---

## Catatan / Pertanyaan Tambahanku:
*(Tulis jika ada yang masih membingungkan)*
