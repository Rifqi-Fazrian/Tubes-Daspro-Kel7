# Program top up

from validasiGame import *
from csvFuncs import *

users = csvReader('user.csv')

cariUser = input('Masukkan username: ')
jumlahTopUp = int(priceFormatNeg(input('Jumlah Topup: ')) )

foundUser = False
for i in range(1, lengthFinder(users)):
    if users[i][1] == cariUser:
        foundUser = True
        if (int(users[i][5]) + jumlahTopUp) >= 0:
            users[i][5] = int(users[i][5]) + jumlahTopUp
            print(f"Top up berhasil, saldo {users[i][1]} menjadi {users[i][5]}")
        else:
            print("Saldo tidak dapat dikurangi sampai negatif")

if not foundUser:
    print(f"User {cariUser} tidak ditemukan")
