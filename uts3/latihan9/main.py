from utils import rata_mahasiswa

jumlah = int(input("Masukkan Jumlah Mahasiswa: "))
for i in range(1, jumlah + 1):
    nilai = input(f"Masukkan Nilai Mahasiswa {i}: ")
    print(f"Rata - Rata Nilai Mahasiswa {i}: {rata_mahasiswa(nilai)}")