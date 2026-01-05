import os
from fungsi import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()
    print("=== MENU BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Trapesium")
    print("7. Belah Ketupat")
    print("8. Layang-layang")
    print("9. Segi Lima")
    print("10. Segi Enam")
    print("11. Keluar")

    pilih = int(input("\nPilih bangun datar: "))

    if pilih == 1:
        s = float(input("Masukkan sisi: "))
        luas, kel = persegi(s)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 2:
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        luas, kel = persegi_panjang(p, l)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 3:
        a = float(input("Alas: "))
        t = float(input("Tinggi: "))
        s1 = float(input("Sisi 1: "))
        s2 = float(input("Sisi 2: "))
        luas, kel = segitiga(a, t, s1, s2)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 4:
        r = float(input("Jari-jari: "))
        luas, kel = lingkaran(r)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 5:
        a = float(input("Alas: "))
        t = float(input("Tinggi: "))
        s = float(input("Sisi miring: "))
        luas, kel = jajar_genjang(a, t, s)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 6:
        a = float(input("Sisi atas: "))
        b = float(input("Sisi bawah: "))
        t = float(input("Tinggi: "))
        s1 = float(input("Sisi miring 1: "))
        s2 = float(input("Sisi miring 2: "))
        luas, kel = trapesium(a, b, t, s1, s2)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 7:
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        s = float(input("Sisi: "))
        luas, kel = belah_ketupat(d1, d2, s)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 8:
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        s1 = float(input("Sisi 1: "))
        s2 = float(input("Sisi 2: "))
        luas, kel = layang_layang(d1, d2, s1, s2)
        print("Luas:", luas)
        print("Keliling:", kel)

    elif pilih == 9:
        s = float(input("Sisi: "))
        print("Keliling:", segi_lima(s))

    elif pilih == 10:
        s = float(input("Sisi: "))
        print("Keliling:", segi_enam(s))

    elif pilih == 11:
        print("Terima kasih 🙏")
        break

    else:
        print("Pilihan tidak valid")

    input("\nTekan ENTER untuk kembali ke menu...")