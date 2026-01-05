from utils import total_harga, hitung_diskon

harga = input("Masukkan Daftar Harga Barang yang dibeli: ")
total = total_harga(harga)
diskon = hitung_diskon(total)
print("Total Pembayaran:", total)
print("Diskon:", diskon)
print("Total Pembayaran Setelah Diskon:", total - diskon)
print()