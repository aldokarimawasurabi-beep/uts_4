from utils import rata_rata, keterangan_lulus

nilai = input("Masukkan Daftar Nilai Tugas Mahasiswa: ")
standar = int(input("Masukkan Standar Kelulusan: "))
rata = rata_rata(nilai)
print("Nilai Rata - Rata:", rata)
print("Keterangan:", keterangan_lulus(rata, standar))
print()