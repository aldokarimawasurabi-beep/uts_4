from constants import MENU
from utils import clear_screen, pause
from inputs import *
from outputs import *
from services import *

def main():
    antrian = []

    while True:
        clear_screen()
        tampilkan_menu(MENU)
        pilihan = input_pilihan()

        if pilihan == "1":
            nama = input_nama()
            tambah_antrian(antrian, nama)
            antrian_ditambahkan(nama)

        elif pilihan == "2":
            nama = panggil_antrian(antrian)
            if nama:
                tampilkan_panggilan(nama)
            else:
                antrian_kosong()

        elif pilihan == "3":
            tampilkan_antrian(antrian)

        elif pilihan == "4":
            print("Keluar dari program")
            break

        else:
            print("Pilihan tidak valid")

        pause()

if __name__ == "__main__":
    main()