from validasiGame import *
from csvFuncs import *

fileUsed = csvReader('game.csv')

nama_game = input("Masukkan nama game: ")
kategori_game = input("Masukkan kategori game: ")
tahun_game = input("Masukkan tahun rilis game: ")
harga_game = input("Masukkan harga game: ")
stok_game = input("Masukkan stok awal: ")

validGame = False
while not validGame:    # Selama ada kolom yang tidak valid maka proses akan diulang sampai semuanya valid
    if isGameAlreadyHere(nama_game, fileUsed):
        print("Game sudah ada di toko, mohon tambahkan game lain")
        nama_game = input("Masukka nama game: ")
        kategori_game = input("Masukkan kategori game: ")
        tahun_game = input("Masukkan tahun rilis game: ")
        harga_game = input("Masukkan harga game: ")
        stok_game = input("Masukkan stok awal: ")
    else:
        if isValidStok(stok_game) and isValidHarga(harga_game) and isValidKategori(kategori_game) and isValidName(nama_game) and isValidTahun(tahun_game):
            validGame = True
        else:
            print("Mohon isi data game dengan sesuai")
            nama_game = input("Masukka nama game: ")
            kategori_game = input("Masukkan kategori game: ")
            tahun_game = input("Masukkan tahun rilis game: ")
            harga_game = input("Masukkan harga game: ")
            stok_game = input("Masukkan stok awal: ")

# Bagian yang menambahkan game ke csv #TODO
# menambahkan ID GXXX ke csv, max ID adalah G999


list_of_id = [0 for i in range(lengthFinder(fileUsed)-1)]     # inisialisasi array semua id yang ada di csv

for i in range(1, lengthFinder(fileUsed)):              # listing semua id yang ada
    list_of_id[i-1] = IDIdentifier(fileUsed[i][0])

newID = 0           # penentuan id baru untuk game baru
for i in range(1, 999+1):
    if i not in list_of_id:
        newID = i
        break

newID = str(newID)              # pemberian nilai fix ID untuk game yang baru
if lengthFinder(newID) == 3:
    newID = "G" + newID
elif lengthFinder(newID) == 2:
    newID = "G0" + newID
else:
    newID = "G00" + newID



fileUsed += [[newID, nama_game, kategori_game, tahun_game, harga_game, stok_game]]
print("Daftar game yang sudah diperbarui: ")
print(fileUsed)
print()
print(f"Selamat! Berhasil menambahkan game {nama_game}")


