from contextlib import nullcontext
import sys


def tambah(a, b):
    hasil = a + b
    return hasil

def tolak(a, b):
    hasil = b - a
    return hasil

def darab(a, b):
    hasil = a * b
    return hasil

def bahagi(a, b):
    hasil = a / b
    return hasil

def pilihan(tambah, tolak, darab, bahagi, pilih):

    a = 0
    b = 0

    if (pilih == "tambah"):
        return tambah(a, b)
    elif (pilih == "tolak"):
        return tolak(a, b)
    elif (pilih == "darab"):
        return darab(a, b)
    elif (pilih == "bahagi"):
        return bahagi(a, b)

def get_input():
    a = sys.argv[1]
    b = sys.argv[2]
    pilih = sys.argv [3]
    return int(a), int(b), str(pilih)

def main():
    a, b, pilih = get_input()
    hasil = pilihan(a,b,pilih)
    print(hasil)

main()