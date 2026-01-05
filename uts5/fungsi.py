import math

def kubus(s):
    return s**3, 6*s**2

def balok(p, l, t):
    return p*l*t, 2*(p*l + p*t + l*t)

def tabung(r, t):
    return math.pi*r*r*t, 2*math.pi*r*(r+t)

def kerucut(r, t):
    s = math.sqrt(r*r + t*t)
    return (1/3)*math.pi*r*r*t, math.pi*r*(r+s)

def bola(r):
    return (4/3)*math.pi*r**3, 4*math.pi*r*r

def prisma_segitiga(a, ts, tp):
    return 0.5*a*ts*tp

def prisma_segiempat(p, l, t):
    return p*l*t

def limas_segiempat(s, t):
    return (1/3)*s*s*t

def limas_segitiga(a, ts, tl):
    return (1/3)*0.5*a*ts*tl

def kerucut_terpancung(r1, r2, t):
    return (1/3)*math.pi*t*(r1**2 + r1*r2 + r2**2)