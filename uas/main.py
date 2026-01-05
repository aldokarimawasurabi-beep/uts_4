# main.py

import os
from utils import nilai_ke_label, label_ke_bobot, hitung_ip

biodata = {}
sks_list = []
nilai_list = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("------------Menu Utama------------")
    print("1. Biodata")
    print("2. SKS")
    print("3. Input Nilai")
    print("4. Lihat Nilai")
    print("5. Lihat IP")
    print("6. Keluar")

while True:
    clear()
    menu()
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        print("------------------Biodata Mahasiswa------------------")
        mode = input("Lihat Biodata atau Input Biodata? (1/2): ")
        if mode == "1":
            print(f"Nama: {biodata.get('nama', '-')}")
            print(f"NIM: {biodata.get('nim', '-')}")
        elif mode == "2":
            biodata['nama'] = input("Nama: ")
            biodata['nim'] = input("NIM: ")
    elif pilihan == "2":
        print("------------------Input SKS------------------")
        sks_input = input("SKS (pisahkan dengan spasi): ")
        sks_list = list(map(int, sks_input.split()))
    elif pilihan == "3":
        print("-------------Input Nilai Mahasiswa-------------")
        mode = input("Input dalam bentuk angka atau huruf? (1/2): ")
        nilai_list.clear()
        if mode == "1":
            nilai_input = input("Nilai (angka, pisahkan dengan spasi): ")
            angka_list = list(map(int, nilai_input.split()))
            nilai_list = [nilai_ke_label(n) for n in angka_list]
        elif mode == "2":
            huruf_input = input("Nilai (huruf, pisahkan dengan spasi): ")
            nilai_list = huruf_input.upper().split()
    elif pilihan == "4":
        print("------------Nilai Mahasiswa (huruf)------------")
        print(f"Nama: {biodata.get('nama', '-')}")
        print(f"NIM: {biodata.get('nim', '-')}")
        print(f"Nilai: {nilai_list}")
    elif pilihan == "5":
        ip = hitung_ip(nilai_list, sks_list)
        print(f"IP: {ip}")
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk kembali ke menu...")