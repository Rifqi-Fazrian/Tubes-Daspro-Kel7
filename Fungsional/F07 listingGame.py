from csvFuncs import *
from validasiGame import *

fileUsed = csvReader('game.csv', delimiter=";")

def insertionSortAsc(arr, column):                 # arr adalah array yg dicek, column adalah tahun atau harga yang akan diliat
    for i in range(1+1, lengthFinder(arr)):         # 1+1 karena header tidak dihitung
        key = int(arr[i][column])
        temp = arr[i]
        j = i-1
        while j>=0+1 and key < int(arr[j][column]):     # 0 + 1 karena header tidak dihitung
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

def selectionSortDesc(arr, column):
    N = lengthFinder(arr)
    for i in range(1,N):
        maks = i

        for j in range(i+1, N):
            if (int(arr[j][column]) > int(arr[maks][column])):
                maks = j

        temp = arr[i]
        arr[i] = arr[maks]
        arr[maks] = temp
    return arr


tabel = [["Game", "Year"],["Valorant", "2020"], ["Overwatch", "2016"], ["Fortnite", "2015"], ["Pong", '1980']]
# tabel buat testng^

def listing(games):
    scheme = input("Masukkan skema sorting: ")
    if scheme.lower() == "tahun+":
        sortedGames = insertionSortAsc(games, 3)  # 3 mewakilkan kolom tahun
        return sortedGames

    elif scheme.lower() == "tahun-":
        sortedGames = selectionSortDesc(games, 3) # 3 mewakilkan kolom tahun
        return sortedGames

    elif scheme.lower() == "harga+":
        sortedGames = insertionSortAsc(games, 4)  # 3 mewakilkan kolom tahun
        return sortedGames

    elif scheme.lower() == "harga-":
        sortedGames = selectionSortDesc(games, 4)  # 3 mewakilkan kolom tahun
        return sortedGames



result = listing(fileUsed)
for game in result:
    print(game)




