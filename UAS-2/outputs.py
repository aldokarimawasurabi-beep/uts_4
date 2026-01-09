def tampilkan_menu(menu):
    print(menu)

def antrian_ditambahkan(nama):
    print(f"Antrian '{nama}' berhasil ditambahkan")

def tampilkan_panggilan(nama):
    print(f"Memanggil : {nama}")

def antrian_kosong():
    print("Antrian kosong")

def tampilkan_antrian(data):
    print("Daftar Antrian:")
    if not data:
        print("Antrian kosong")
    else:
        for i, nama in enumerate(data, 1):
            print(f"{i}. {nama}")