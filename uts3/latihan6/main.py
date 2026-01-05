from utils import total_belanja, pajak

harga = input("Masukkan Daftar Harga Barang yang dibeli: ")
total = total_belanja(harga)
pajak_barang = pajak(total)
print("Total Pembayaran:", total)
print("Pajak:", pajak_barang)
print("Total Pembayaran Setelah Pajak:", total + pajak_barang)
print()