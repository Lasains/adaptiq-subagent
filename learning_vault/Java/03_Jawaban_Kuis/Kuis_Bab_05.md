# 📝 Jawaban Kuis — Bab 5: Perulangan

> Tulis jawabanmu di bawah ini, lalu kabari tutormu untuk dikoreksi!

---

## Soal 1 — Pilihan Ganda (10 poin)
**Jawabanku**: D

**Alasanku**: karena i nya tidak pernah di update sehingga kondisinya selalu treu dan terjadi infinite loop

---

## Soal 2 — Jejak Eksekusi `while` (25 poin)

| Iterasi | Nilai `skor` | Cek `skor <= 5` |    Output     | `skor` setelah `+= 2` |
| :-----: | :----------: | :-------------: | :-----------: | :-------------------: |
|    1    |      1       |      true       |       1       |           3           |
|    2    |      3       |      true       |       3       |           5           |
|    3    |      5       |      true       |       5       |           7           |
|    4    |      7       |      false      | Loop berhenti |           —           |

---

## Soal 3 — Prediksi Output `break` & `continue` (30 poin)

Output program (tulis satu angka per baris):
```
1
2
4
5
```

**Alasanku** (jelaskan kenapa angka 3 dan 6 tidak muncul): karena angka 3 itu di skip dikarenakan terdapat kondisi dimana jika i == 3 maka dia continue(skip) sedangkan 6 loop harus berhenti karena terdapat kondisi jika i == 6 maka dia break(stop)

---

## Soal 4 — Coding Mini (35 poin)

```java
public class PolaBintang{
	public static void main(String[] args){
		for(int i = 5; i >= 1;i--){
			for(int j = 0; j<i;j++){
				System.out.println("*");
			}
		}
	}
}
```

---

## Catatan / Pertanyaan Tambahanku:
*(Tulis jika ada yang masih membingungkan)*
