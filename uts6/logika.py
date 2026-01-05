def nilai_ke_label(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def label_ke_bobot(label):
    label = label.upper()
    if label == "A":
        return 4
    elif label == "B":
        return 3
    elif label == "C":
        return 2
    elif label == "D":
        return 1
    elif label == "E":
        return 0
    else:
        return None


def hitung_total_sks(sks):
    return sum(sks)


def hitung_total_nilai(bobot, sks):
    total = 0
    for i in range(len(bobot)):
        total += bobot[i] * sks[i]
    return total


def hitung_ips(total_nilai, total_sks):
    if total_sks == 0:
        return 0
    return total_nilai / total_sks