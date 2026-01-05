def total_harga(harga_str):
    return sum(int(h) for h in harga_str.split())

def hitung_diskon(total, persen=10):
    return total * persen / 100