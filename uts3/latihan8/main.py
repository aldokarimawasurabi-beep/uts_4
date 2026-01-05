from utils import total_konsumen

jumlah = int(input("Masukkan Jumlah Konsumen: "))
for i in range(1, jumlah + 1):
    harga = input(f"Masukkan Harga Barang yang dibeli Konsumen {i}: ")
    print(f"Total Pembayaran Konsumen {i}: {total_konsumen(harga)}")
print()