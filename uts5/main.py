import os
from fungsi import *

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()
    print("=== MENU BANGUN RUANG ===")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")
    print("6. Prisma Segitiga")
    print("7. Prisma Segiempat")
    print("8. Limas Segiempat")
    print("9. Limas Segitiga")
    print("10. Kerucut Terpancung")
    print("11. Keluar")

    pilih = int(input("\nPilih bangun ruang: "))

    if pilih == 1:
        s = float(input("Masukkan sisi: "))
        v, l = kubus(s)
        print("Volume:", v)
        print("Luas permukaan:", l)

    elif pilih == 2:
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        v, lp = balok(p, l, t)
        print("Volume:", v)
        print("Luas permukaan:", lp)

    elif pilih == 3:
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        v, l = tabung(r, t)
        print("Volume:", v)
        print("Luas permukaan:", l)

    elif pilih == 4:
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        v, l = kerucut(r, t)
        print("Volume:", v)
        print("Luas permukaan:", l)

    elif pilih == 5:
        r = float(input("Jari-jari: "))
        v, l = bola(r)
        print("Volume:", v)
        print("Luas permukaan:", l)

    elif pilih == 6:
        a = float(input("Alas segitiga: "))
        ts = float(input("Tinggi segitiga: "))
        tp = float(input("Tinggi prisma: "))
        print("Volume:", prisma_segitiga(a, ts, tp))

    elif pilih == 7:
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segiempat(p, l, t))

    elif pilih == 8:
        s = float(input("Sisi alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", limas_segiempat(s, t))

    elif pilih == 9:
        a = float(input("Alas segitiga: "))
        ts = float(input("Tinggi segitiga: "))
        tl = float(input("Tinggi limas: "))
        print("Volume:", limas_segitiga(a, ts, tl))

    elif pilih == 10:
        r1 = float(input("Jari-jari atas: "))
        r2 = float(input("Jari-jari bawah: "))
        t = float(input("Tinggi: "))
        print("Volume:", kerucut_terpancung(r1, r2, t))

    elif pilih == 11:
        print("Terima kasih 🙏")
        break

    else:
        print("Pilihan tidak valid")

    input("\nTekan ENTER untuk kembali ke menu...")