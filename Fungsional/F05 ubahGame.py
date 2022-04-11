# Fungsi yang mengubah data sebuah game pada csv
from validasiGame import *
from csvFuncs import *

fileUsed = csvReader('game.csv')

def ubahGame(listOfGames):   # menerima sebuah csv game dan mengganti kandungannya kecuali stok
    ID = input("Masukkan ID game: ")
    found = False
    index = 0
    for i in range(lengthFinder(listOfGames)):
        if listOfGames[i][0] == ID:
            found = True
            validGame = False       # proses while untuk memvalidasi elemen game
            while not validGame:    # validasi elemen-elemen game benar atau tidak
                tempName = input("Masukkan nama game: ")
                if tempName != "":
                    tempVal1 = isValidName(tempName)
                else:
                    tempVal1 = True
                    tempName = listOfGames[i][1]

                tempKategori = input("Masukkan kategori game: ")
                if tempKategori != "":
                    tempVal2 = isValidKategori(tempKategori)
                else:
                    tempVal2 = True
                    tempKategori = listOfGames[i][2]

                tempTahun = input("Masukkan tahun rilis game: ")
                if tempTahun != "":
                    tempVal3 = isValidTahun(tempTahun)
                else:
                    tempVal3 = True
                    tempTahun = listOfGames[i][3]

                tempHarga = input("Masukkan harga game: ")
                if tempHarga != "":
                    tempVal4 = isValidHarga(tempHarga)
                else:
                    tempVal4 = True
                    tempHarga = listOfGames[i][4]

                if tempVal4 and tempVal3 and tempVal2 and tempVal1:
                    validGame = True    #bila semua elemen sudah sesuai program lanjut ke editing
                else:
                    print("Data tidak sesuai, coba lagi")

            listOfGames[i][1] = tempName        # nilai sudah valid, dimasukkan ke csv yang sesuai
            listOfGames[i][2] = tempKategori
            listOfGames[i][3] = tempTahun
            listOfGames[i][4] = tempHarga
            index = i
            break
    if not found:
        print("Maaf ID game tidak ditemukan")
    else:
        print("Game berhasil diperbarui, berikut info terbarunya:  ")
        print(listOfGames[index])



ubahGame(fileUsed)
