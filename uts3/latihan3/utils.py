def rata_rata(nilai_str):
    data = nilai_str.split()
    return sum(int(n) for n in data) / len(data)

def keterangan_lulus(rata, standar):
    return "Lulus" if rata >= standar else "Tidak Lulus"