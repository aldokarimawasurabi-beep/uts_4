def total_pembayaran(harga_str):
    return sum(int(h) for h in harga_str.split())