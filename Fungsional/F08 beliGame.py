from csvFuncs import *
from validasiGame import *

def cekID(ID, games):       # ngecek apakah ID game ada pada daftar game
    found = False
    for i in range(1, lengthFinder(games)):     # dimulai dari satu karena header tidak dicek
        if games[i][0] ==  ID:
            found = True
            break
    return found

def usersOwn(gameID, kepemilikan):                      # mengecek id user berapa saja yang memiliki suatu game
    found = False
    for i in range(1, lengthFinder(kepemilikan)):       # dimulai dari satu karena header tidak dicek
        if gameID ==  kepemilikan[i][0]:
            owners = splitter(kepemilikan[i][1], delimiter=",")  # id yang disimpan dalam kepemilikan dipisah oleh koma
            found = True
            break
    if found:
        return owners
    else:
        return "ID Game tidak ditemukan"


def cekKepemilikan(IDGame, userID, listGame, listKepemilikan):      # mengecek csv kepemilikan untuk user yg udh terlogin
    if cekID(IDGame, listGame):                                     # dicek dulu apakah gamenya ada
        gameOwners = usersOwn(IDGame, listKepemilikan)              # semua pemilik dari game dimasukkan ke dalam list
        found = False                                               # inisialisasi status kepemilikan

        for i in range(lengthFinder(gameOwners)):                   # mencari jika id user yang dicek punya game tsb
            if str(userID) == gameOwners[i]:
                found = True
                break
        return found
    else:
        return "ID Game tidak ditemukan!"                           # game gk ada di game.csv

def cekSaldo(userID, userList)     :                 # ngecek nilai saldo suatu user
    for i in range(1, lengthFinder(userList)):      # dimulai dari satu karena header tidak dicek
        if userList[i][0] == str(userID):
            return userList[i][5]

def cekStok(gameID, gameList):
    for i in range(1, lengthFinder(gameList)):
        if gameList[i][0] == str(gameID):
            return gameList[i][5]

def gameIDidentifier(gameID, gameList):
    for i in range(lengthFinder(gameList)):
        if gameID == gameList[i][0]:
            return gameList[i][1]

def gamePriceidentifier(gameID, gameList):
    for i in range(lengthFinder(gameList)):
        if gameID == gameList[i][0]:
            return gameList[i][4]

def gameIndexidentifier(gameID, gameList):
    indexFound = 0
    for i in range(lengthFinder(gameList)):
        if gameList[i][0] == gameID:
            indexFound = i
    return indexFound

def addOwner(userID, gameID, kepemilikan):              # masukkan id user ke kepemilikan
    for i in range(lengthFinder(kepemilikan)):
        if gameID == kepemilikan[i][0]:
            kepemilikan[i][1] += f',{userID}'

def addRiwayat(userID, gameID, gameList, purchaseList):
    index = int(gameIndexidentifier(gameID, gameList))
    purchaseList += [[gameID, gameList[index][1], gameList[index][4], userID, 2022]]


dataGame = csvReader('game.csv', delimiter=";")
dataUser = csvReader('user.csv', delimiter=";")
dataKepemilikan = csvReader('kepemilikan.csv', delimiter=";")
dataRiwayat = csvReader('riwayat.csv', delimiter=";")

loggedUserID = dataUser[1][0]

gameID = input("Masukkan ID Game (format GXXX): ")

if cekID(gameID, dataGame):
    stok = int(cekStok(gameID, dataGame))
    if stok > 0:
        saldo = int(cekSaldo(loggedUserID, dataUser))

        if saldo > int(gamePriceidentifier(gameID, dataGame)):

            if not cekKepemilikan(gameID, loggedUserID, dataGame, dataKepemilikan):
                gameName = gameIDidentifier(gameID, dataGame)
                print(f"Anda berhasil membeli game {gameName}!")
                addedGameUser = loggedUserID
                addOwner(loggedUserID, gameID, dataKepemilikan)             # data kepemilikan diperbarui
                addRiwayat(loggedUserID, gameID, dataGame, dataRiwayat)     # Data riwayat diperbarui
            else:
                print("Anda sudah memiliki game tersebut!")

        else:
            print("Saldo Anda tidak cukup")

    else:
        print("Stok game habis!")

else:
    print("ID game tidak ditemukan")


print(dataKepemilikan)
print(dataRiwayat)

#TODO save func



