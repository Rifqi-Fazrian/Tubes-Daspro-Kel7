from validasiGame import *
from csvFuncs import *

fileUsed = csvReader('game.csv', delimiter=";")


def ubahStok(games):
    IDCheck = input("Masukkan ID game: ")
    foundIndex = IDFinder(IDCheck, games)
    if foundIndex != -999:
        newStock = int(input(f"Tambahkan atau kurangkan stok game {games[foundIndex][1]}: "))
        if ((int(games[foundIndex][5])) + newStock)>=0:
            games[foundIndex][5] = str(int(games[foundIndex][5]) + newStock)
            print(f"Stock game {games[foundIndex][1]} berhasil diubah. Stock sekarang {games[foundIndex][5]} ")
        else:
            print(f"Stock game {games[foundIndex][1]} gagal diubah karena stok kurang. Stock sekarang {games[foundIndex][5]}")
    else:
        print("ID game tidak ditemukan")

ubahStok(fileUsed)

