def tambah_kendaraan(data, kendaraan):
    data.append(kendaraan)

def cari_kendaraan(data, plat):
    for k in data:
        if k["plat"] == plat:
            return k
    return None

def hapus_kendaraan(data, kendaraan):
    data.remove(kendaraan)