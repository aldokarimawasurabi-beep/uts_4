import math

def persegi(sisi):
    return sisi * sisi, 4 * sisi

def persegi_panjang(panjang, lebar):
    return panjang * lebar, 2 * (panjang + lebar)

def segitiga(alas, tinggi, s1, s2):
    return 0.5 * alas * tinggi, alas + s1 + s2

def lingkaran(r):
    return math.pi * r * r, 2 * math.pi * r

def jajar_genjang(alas, tinggi, sisi):
    return alas * tinggi, 2 * (alas + sisi)

def trapesium(a, b, t, s1, s2):
    return 0.5 * (a + b) * t, a + b + s1 + s2

def belah_ketupat(d1, d2, sisi):
    return 0.5 * d1 * d2, 4 * sisi

def layang_layang(d1, d2, s1, s2):
    return 0.5 * d1 * d2, 2 * (s1 + s2)

def segi_lima(sisi):
    return 5 * sisi

def segi_enam(sisi):
    return 6 * sisi