import os

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nTekan ENTER untuk melanjutkan...")