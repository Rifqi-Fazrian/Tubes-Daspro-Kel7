#Program mencari game

from validasiGame import *
from csvFuncs import *

def printGame(listGame, i):
    print(f'ID Game : {listGame[i][0]}')
    print(f'Nama Game : {listGame[i][1]}')
    print(f'Kategori Game : {listGame[i][2]}')
    print(f'Tahun Terbit Game : {listGame[i][3]}')
    print(f'Harga Game : {listGame[i][4]}')
    print("---------------")
    print()



search_my_game = csvReader('game.csv')
cariId = input("ID Game : ")
cariTahun = input('Tahun Game : ')
found = False

print("Daftar game pada inventory yang memenuhi kriteria:")

for i in range (1,lengthFinder(search_my_game)):
    if cariTahun == '' and cariId != '':        # hanya ada filter ID
        if search_my_game[i][0] == cariId:
            printGame(search_my_game, i)
            found = True

    elif cariTahun != '' and cariId == '':      # hanya ada filter tahun
        if str(search_my_game[i][3]) == str(cariTahun):
            printGame(search_my_game, i)
            found = True

    elif cariTahun != '' and cariId != '':      # kedua filter jalan
        if str(search_my_game[i][3]) == str(cariTahun) and search_my_game[i][0] == cariId:
            printGame(search_my_game, i)
            found = True

    else:   # tidak ada filter
        printGame(search_my_game, i)
        found = True

if not found:
    print("Tidak ada game yang memenuhi kriteria tersebut")
