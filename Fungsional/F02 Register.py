# Program Fungsi Register

# Program dapat mendaftarkan pengguna baru dengan memasukkan nama, username, dan password.
# Username harus unik (tidak bisa ada username yang sama)

# TODO
# Belum memahami cara menyimpan data ke dalam csv

from csvFuncs import *
from validasiGame import *

def register(user, data):
    if (user[4].lower() == "admin") :
        nama = input("Masukkan nama : ")
        username = input("Masukkan username : ")
        # username harus unik
        # inisialisasi i
        i = 0
        while (i < lengthFinder(data)) :
            cek_username = data[i]
            if (username == cek_username[1]) :
                print ("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
                i = 0
                username = input("Masukkan username : ")
            else :
                i += 1
        password = input("Masukkan password user : ")

        #Penambahan ID user baru
        list_of_id = [0 for i in range(lengthFinder(data) - 1)]  # inisialisasi array semua id yang ada di csv

        for i in range(1, lengthFinder(data)):                  # listing semua id yang ada
            list_of_id[i - 1] = int(data[i][0])

        newID = 0                                               # penentuan id baru untuk game baru
        for i in range(1, 999 + 1):
            if i not in list_of_id:
                newID = i
                break

        saldo = "0"

        user[i] = [newID, username, nama, password, "user", saldo]
        print("Username" + username + " telah berhasil register kedalam Binomo")
        print(user[i])

userList = csvReader('user.csv', delimiter=";")

user = userList[1]
register(user, userList)
