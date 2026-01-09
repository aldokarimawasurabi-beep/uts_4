def tampilkan_menu(menu):
    print(menu)

def sukses_tambah():
    print("Berhasil menambahkan kendaraan")

def kendaraan_tidak_ditemukan():
    print("Kendaraan tidak ditemukan")

def kendaraan_keluar(data):
    print("Kendaraan keluar:")
    print(f"Plat  : {data['plat']}")
    print(f"Jenis : {data['jenis']}")
    print(f"Merk  : {data['merk']}")

def tampilkan_parkir(data):
    print("Daftar Parkir:")
    if not data:
        print("Parkir kosong")
    else:
        for i, k in enumerate(data, 1):
            print(f"{i}. {k['plat']} - {k['jenis']} - {k['merk']}")