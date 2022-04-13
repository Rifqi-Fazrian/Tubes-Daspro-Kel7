from csvFuncs import *


def isValidName(nama):
    stringNama = str(nama)          # untuk nama game yang hanya angka dibuat menajadi string
    panjangNama = lengthFinder(stringNama)   # panjang dari string nama game
    namaValid = False
    if panjangNama>0:               # nama tidak boleh kosong
        i = 1
        while i < panjangNama and not namaValid:
            if stringNama[i] in "abcdefghijklmnopqrstuvwxyz" or stringNama[i] in "1234567890":  #syarat nama adalah harus memiliki angka atau huruf
                namaValid = True
                break
            else:
                i += 1
        return namaValid
    else:
        return namaValid

def isValidKategori(kategori):
    stringKategori = str(kategori)
    panjangKategori = lengthFinder(stringKategori)
    kategoriValid = True
    if panjangKategori>0:        # kategori tidak boleh kosong
        i = 1
        while i < panjangKategori and kategoriValid:
            if not (97<= ord(stringKategori[i]) <= 122) and not (65 <= ord(stringKategori[i]) <=90) and stringKategori[i] not in " -_" and (stringKategori[0] != " "):  #syarat kategori adalah segalanya harus huruf dan tanda - _
                kategoriValid = False
                break
            else:
                i += 1
        return kategoriValid
    else:
        kategoriValid = False
        return kategoriValid


def isValidTahun(year):
    stringTahun = str(year)
    panjangTahun = lengthFinder(stringTahun)
    tahunValid = True
    if panjangTahun>0:
        i = 1
        while i < panjangTahun and tahunValid:
            if stringTahun[i] not in "1234567890":  # syarat tahun adalah harus berupa angka
                tahunValid = False
                break
            else:
                i += 1
    else:
        tahunValid = False


    # setelah dicek apakah isinya angka semua, tahun akan dicek validasinya
    # tahun yang valid bagi rilis game adalah di antara 1950 sampai 2022 (tahun ini)
    if tahunValid:
        if not (1950<=int(year)<=2022):
            tahunValid = False
    return tahunValid


def isValidHarga(price):
    stringHarga = str(price)
    panjangHarga = lengthFinder(str(price))
    validHarga = True
    newString = ""
    for i in range(panjangHarga):
        if stringHarga[i] in "!@#$%^&*()-+=-abcdefghijklmnopqrstuvwxyz":      # tidak boleh negatif atau mengandung simbol/huruf
            validHarga = False
    if validHarga:
        for i in range(panjangHarga):
            if stringHarga[i] in "1234567890":      # proses ini menghilangkan semua tanda pemisah titik koma
                newString += stringHarga[i]

        if int(newString) > 0:
            validHarga = True

    return validHarga

def priceFormat(price):
    stringPrice = str(price)
    result = ''
    for number in stringPrice:
        if number in "1234567890":
            result += number
    return result

def priceFormatNeg(price):
    stringPrice = str(price)
    result = ''
    for number in stringPrice:
        if number in "-1234567890":
            result += number
    return result

priceFormat("200.000")

def isValidStok(stock):
    if lengthFinder(stock) > 0:
        for i in range(lengthFinder(stock)):
            if stock[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=":
                return False
        if int(stock) >= 0:
            return True
        else:
            return False
    else:
        return False

def IDIdentifier(ID):           # unuk mengubah format id menjadi angka
    IDResult = 0
    if ID[1] == "0":
        if ID[2] == "0":        # maka id pasti satuan
            IDResult = int(ID[3])
        else:                   # maka id merupakan puluhan
            IDResult = int(ID[2] + ID[3])
    else:
        IDResult = str(ID[1]+ ID[2] + ID[3])
    return IDResult

def isGameAlreadyHere(dicek, listgames):
    same = False
    for i in range(lengthFinder(listgames)):
        if (dicek).upper() == listgames[i][1].upper():
            same = True
            break
    return same


def IDFinder(dicek, listgames):
    index = -999
    for i in range(lengthFinder(listgames)):
        if (dicek).upper() == listgames[i][0].upper():
            index = i
            break
    return index












