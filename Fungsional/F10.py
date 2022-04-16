# Program mencari game yang dimiliki user

from validasiGame import *
from csvFuncs import *

def printGame(print_inventory, i):
    print(f'ID Game : {print_inventory[i][0]}')
    print(f'Nama Game : {print_inventory[i][1]}')
    print(f'Kategori Game : {print_inventory[i][2]}')
    print(f'Tahun Terbit Game : {print_inventory[i][3]}')
    print(f'Harga Game : {print_inventory[i][4]}')
    print("---------------")
    print()

loggedUserID = 1        #TODO implementasikan logged in user ID
gameStore = csvReader("game.csv", delimiter=";")
ownership = csvReader("kepemilikan.csv", delimiter=";")

def IDLister(kepemilikan):
    IDlist = []
    for i in range(1,lengthFinder(ownership)):
        IDlist += [kepemilikan[i][1]]
    return IDlist

list_of_ids = IDLister(ownership)

def search_games(games):
    cariID = input("Masukkan ID game: ")
    cariTahun = input("Masukkan tahun rilis game: ")
    gameList = []
    found = False
    for i in range(1, lengthFinder(games)):
        if cariTahun == '' and cariID != '':        # hanya ada filter ID
            if games[i][0] == cariID:
                gameList += [games[i]]
                found = True

        elif cariTahun != '' and cariID == '':      # hanya ada filter tahun
            if str(games[i][3]) == str(cariTahun):
                gameList += [games[i]]
                found = True

        elif cariTahun != '' and cariID != '':      # kedua filter jalan
            if str(games[i][3]) == str(cariTahun) and games[i][0] == cariID:
                gameList += [games[i]]
                found = True

        else:  # tidak ada filter
            gameList += [games[i]]
            found = True

    if found:
        return gameList
    else:
        return "Tidak ada game yang memenuhi kriteria"


gameFound = search_games(gameStore)     # data game yang memenuhi kriteria

foundGames = 0
for i in range(lengthFinder(gameFound)):
    for j in range(lengthFinder(ownership)):
        if gameFound[i][0] == ownership[j][0]:
            if str(loggedUserID) in list_of_ids[j-1]:
                foundGames += 1
                printGame(gameFound, i)
if foundGames == 0:
    print("Tidak ada game yang memenuhi kriteria")

