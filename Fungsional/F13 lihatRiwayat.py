from csvFuncs import *

riwayat = csvReader('riwayat.csv', delimiter=";")
loggedUserID = 1

def printGame(print_history, i):
    print(f'ID Game: {print_history[i][0]}')
    print(f'Nama Game: {print_history[i][1]}')
    print(f'Harga Game: {print_history[i][2]}')
    print(f'Tahun Beli: {print_history[i][4]}')
    print("-----------")
    print()

def findID(userID, riwayat):
    riwayat_games = []
    for i in range(1, lengthFinder(riwayat)):
        if str(userID) in riwayat[i][3]:
            riwayat_games += [riwayat[i][0]]
    return riwayat_games

def printRiwayat(gameHistory, gameList):
    for i in range(lengthFinder(gameHistory)):
        for j in range(1, lengthFinder(gameList)):
            if gameHistory[i] == gameList[j][0]:
                printGame(gameList, j)

user_games = findID(loggedUserID, riwayat)
printRiwayat(user_games, riwayat)