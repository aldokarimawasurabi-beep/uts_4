from constants import MENU
from utils import bersihkan_layar, pause
from inputs import *
from outputs import *
from services import *

def main():
    parkir = []

    while True:
        bersihkan_layar()
        tampilkan_menu(MENU)
        pilihan = input_pilihan()

        if pilihan == "1":
            kendaraan = input_kendaraan()
            tambah_kendaraan(parkir, kendaraan)
            sukses_tambah()

        elif pilihan == "2":
            plat = input_plat_keluar()
            kendaraan = cari_kendaraan(parkir, plat)
            if kendaraan:
                kendaraan_keluar(kendaraan)
                hapus_kendaraan(parkir, kendaraan)
            else:
                kendaraan_tidak_ditemukan()

        elif pilihan == "3":
            tampilkan_parkir(parkir)

        elif pilihan == "4":
            print("Keluar dari program")
            break

        else:
            print("Pilihan tidak valid")

        pause()

if __name__ == "__main__":
    main()