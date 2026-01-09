def tambah_antrian(antrian, nama):
    antrian.append(nama)

def panggil_antrian(antrian):
    if antrian:
        return antrian.pop(0)
    return None