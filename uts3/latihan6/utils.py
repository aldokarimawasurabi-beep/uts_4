def total_belanja(harga_str):
    return sum(int(h) for h in harga_str.split())

def pajak(total, persen=10):
    return total * persen / 100