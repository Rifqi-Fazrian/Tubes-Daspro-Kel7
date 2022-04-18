# Program game yang dimiliki
from csvFuncs import *

ownership = csvReader("kepemilikan.csv", delimiter=";")
gameStore = csvReader("game.csv", delimiter=";")
loggedUserID = 1        #TODO implementasi logged in user

def printGame(print_inventory, i):
    print(f'ID Game : {print_inventory[i][0]}')
    print(f'Nama Game : {print_inventory[i][1]}')
    print(f'Kategori Game : {print_inventory[i][2]}')
    print(f'Tahun Terbit Game : {print_inventory[i][3]}')
    print(f'Harga Game : {print_inventory[i][4]}')
    print("---------------")
    print()


def findGameID(userID, kepemilikan):
    games_owned = []
    for i in range(1, lengthFinder(kepemilikan)):
        if str(userID) in kepemilikan[i][1]:
            games_owned += [kepemilikan[i][0]]
    return games_owned

def printOwnedGames(ownedGames, gameList):
    for i in range(lengthFinder(ownedGames)):
        for j in range(1, lengthFinder(gameList)):
            if ownedGames[i] == gameList[j][0]:
                printGame(gameList, j)

user_games = findGameID(loggedUserID, ownership)
printOwnedGames(user_games, gameStore)


