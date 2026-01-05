def rata_mahasiswa(nilai_str):
    data = nilai_str.split()
    return sum(int(n) for n in data) / len(data)