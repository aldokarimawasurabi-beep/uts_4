def input_pilihan():
    return input("Pilihan : ")

def input_kendaraan():
    plat = input("Plat : ")
    jenis = input("Jenis : ")
    merk = input("Merk : ")
    return {
        "plat": plat,
        "jenis": jenis,
        "merk": merk
    }

def input_plat_keluar():
    return input("Plat Kendaraan : ")