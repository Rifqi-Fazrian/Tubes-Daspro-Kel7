from csvFuncs import *
from validasiGame import *
from roleAccess import *


def login():
    loggedInUserID = 0     # variabel yang akan direturn ketika sudah log in yaitu id user/admin
    # User login memasukkan nama dan password
    fileUsed = csvReader('user.csv')
    loggedIn = False

    command = input("Silahkan ketik login:  ")
    while command.lower() != "login":
        print('Maaf, Anda harus login terlebih dahulu umtuk mengirim perintah selain "login" ')
        command = input("Silahkan ketik login:")

    if command.lower() == "login":
        username = input("Masukkan username: ")
        password = input("Masukkan password user: ")
        newID = 0
        userIndex = 0
        for i in range(1, lengthFinder(fileUsed)):
            if fileUsed [i][1] == username and fileUsed[i][3] == password:
                userIndex = i
                newID = fileUsed[i][0]
                nama = fileUsed[i][2]
                loggedInUserID = newID      # id user yg sudah login disimpan
                loggedIn = True
                print(f"Halo {nama}! Selamat datang di Binomo")

    #TODO jalankan input sesuai permintaan user
    if loggedIn:
        command = input("Masukkan sebuah perintah:  ")
        foundCommand = False
        while not foundCommand:
            if fileUsed[userIndex][4].lower() == 'user':
                if command in user:
                    foundCommand = True
                    print("Perintah diterima")
                elif not (command in user) and command in admin:
                    print("Anda tidak memiliki izin untuk melaksanakan perintah tersebut, silahkan hubungi admin")
                    command = input("Masukkan sebuah perintah: ")
                else:   #   command tidak valid
                    print("perintah tidak dikenal, silahkan dicoba lagi")
                    command = input("Masukkan sebuah perintah: ")


            elif fileUsed[userIndex][4].lower() == 'admin':
                if command in admin:
                    foundCommand = True
                    print("Perintah diterima")
                elif not (command in admin) and command in user:
                    print("Anda harus menjadi user untuk menjalankan perintah tersebut")
                    command = input("Masukkan sebuah perintah: ")
                else:   #   command tidak valid
                    print("perintah tidak dikenal, silahkan dicoba lagi")
                    command = input("Masukkan sebuah perintah: ")

        #TODO perintah dijalankan di bawah if command ditemukan




    if newID == 0:
        print("Passsword atau username salah atau tidak ditemukan.")



login()
