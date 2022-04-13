# Program mencari game di toko

from validasiGame import *
from csvFuncs import *
from validasiGame import priceFormat

def printGame(listGame, i):
    print(f'ID Game : {listGame[i][0]}')
    print(f'Nama Game : {listGame[i][1]}')
    print(f'Kategori Game : {listGame[i][2]}')
    print(f'Tahun Terbit Game : {listGame[i][3]}')
    print(f'Harga Game : {listGame[i][4]}')
    print("---------------")
    print()


search_game_at_store = csvReader ('game.csv')
cariId = input("ID Game: ")
cariNama = input("Nama game: ")
cariTahun = input('Tahun Game : ')
cariKategori = input('Kategori Game : ')
cariHarga = priceFormat(input('Harga Game : '))     # harga diubah kalau ada titik dihilangkan

print(search_game_at_store[0])
print("---------------")

found = False
for i in range (1,lengthFinder(search_game_at_store)):
    if search_game_at_store[i][0] == cariId or cariId == '':
        if search_game_at_store[i][1].upper() == cariNama.upper() or cariNama == '':
            if search_game_at_store[i][2].upper() == cariKategori.upper() or cariKategori == '':
                if search_game_at_store[i][3] ==  cariTahun or cariTahun == '':
                    if search_game_at_store[i][4] == cariHarga or cariHarga == '':
                        printGame(search_game_at_store, i)
                        found = True

if not found:
    print("Tidak ada game yang memenuhi kriteria")
