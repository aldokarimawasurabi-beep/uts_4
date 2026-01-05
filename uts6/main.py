# main.py

import os
from logika import nilai_ke_label, label_ke_bobot, hitung_total_sks, hitung_total_nilai, hitung_ips

matkul = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("menu --------")
    print("1. konversi nilai ke label")
    print("2. konversi label ke bobot")
    print("3. hitung total sks yang diambil")
    print("4. hitung total nilai")
    print("5. hitung IPS")
    print("6. exit")

while True:
    clear_screen()
    menu()
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        nilai = int(input("Nilai Mahasiswa: "))
        label = nilai_ke_label(nilai)
        print(f"Label: {label}")
    elif pilihan == "2":
        label = input("Label: ")
        bobot = label_ke_bobot(label)
        if bobot is not None:
            print(f"Bobot: {bobot}")
        else:
            print("Label tidak valid.")
    elif pilihan == "3":
        print("Masukkan data mata kuliah:")
        matkul.clear()
        while True:
            nama = input("Nama matkul (kosongkan untuk selesai): ")
            if not nama:
                break
            sks = int(input("SKS: "))
            label = input("Label: ")
            matkul.append({'nama': nama, 'sks': sks, 'label': label})
        print(f"Total SKS: {hitung_total_sks(matkul)}")
    elif pilihan == "4":
        print(f"Total Nilai: {hitung_total_nilai(matkul)}")
    elif pilihan == "5":
        print(f"IPS: {hitung_ips(matkul):.2f}")
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")

    input("\nTekan Enter untuk kembali ke menu...")