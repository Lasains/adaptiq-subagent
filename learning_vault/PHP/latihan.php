<?php
function daftarAnggota(string $nama, int $usia): string{
	if($usia < 17){
		throw new InvalidArgumentException($nama . " belum cukup umur (min. 17 tahun)");
	} else if($usia > 60){
		throw new InvalidArgumentException($nama . " melebihi batas usia anggota (max. 60 tahun)");
	}
		return "✅ " . $nama . " berhasil didaftarkan (usia: " . $usia . " tahun).";
}

try{
	echo daftarAnggota("Budi", 25) . "\n";
	echo daftarAnggota("Andi", 17) . "\n";
	echo daftarAnggota("Pak Soekarno", 61) . "\n";
}catch (InvalidArgumentException $e){
	echo "Error: " . $e->getMessage();
}
