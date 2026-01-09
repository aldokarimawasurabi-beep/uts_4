# utils.py

def nilai_ke_label(nilai):
    if 85 <= nilai <= 100:
        return "A"
    elif 80 <= nilai <= 84:
        return "A-"
    elif 75 <= nilai <= 79:
        return "B+"
    elif 70 <= nilai <= 74:
        return "B"
    elif 65 <= nilai <= 69:
        return "B-"
    elif 60 <= nilai <= 64:
        return "C+"
    elif 55 <= nilai <= 59:
        return "C"
    elif 45 <= nilai <= 54:
        return "D"
    else:
        return "E"

def label_ke_bobot(label):
    bobot_map = {
        "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0,
        "B-": 2.7, "C+": 2.3, "C": 2.0, "D": 1.0, "E": 0.0
    }
    return bobot_map.get(label.upper(), 0.0)

def hitung_ip(nilai_list, sks_list):
    total_sks = sum(sks_list)
    total_nilai = sum(label_ke_bobot(n) * s for n, s in zip(nilai_list, sks_list))
    return round(total_nilai / total_sks, 2) if total_sks else 0.0