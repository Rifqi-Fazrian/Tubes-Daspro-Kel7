# untuk menggunakan split function berikut, masukkan parameter data yang akan displit dan delimiter (pemisah)
# panjang data dapat ditentukan dengan menggunakan fungsi lengthFinder

import os

def lengthFinder(string):           # fungsi untuk mencari panjang suatu string (seperti len())
    length = 0
    for i in string:
        length += 1
    return length


def splitter(string, delimiter):  # pengganti fungsi split() karena gk boleh make split
    split_result = []
    temp = ''
    for x in string:
        if x == delimiter or x=="\n":
            split_result += [temp]
            temp = ''
        else:
            temp += x
    if temp:
        split_result += [temp]
    return split_result


def csvReader(filename, delimiter=';'):
    with open(filename) as file:
        parse = []
        for line in file:
            values = splitter(line, delimiter)
            if values != ['']:
                parse += [values]
    return parse

def searcher(dicari, sumber):
    found = False
    for i in range(lengthFinder(sumber)):
        if sumber[i] == dicari:
            found = True
            break
    return found



def findMax(dicari):
    max = -9999
    for i in range(lengthFinder(dicari)):
        if (int(dicari[i]) >= int(max)):
            max = int(dicari[i])
    return max

def findMin(dicari):
    min = 9999
    for i in range(lengthFinder(dicari)):
        if (int(dicari[i]) <= int(min)):
            min = int(dicari[i])
    return min


def write_csv(filename, to_write):
    with open(filename, "w") as file:
        baris = lengthFinder(to_write)
        kolom = lengthFinder(to_write[0])            # Jumlah kolom sama pada tiap baris
        for i in range(baris):
            for j in range(kolom):
                file.write(str(to_write[i][j]))
                if j < kolom-1:
                    file.write(";")                 # pemisah titik koma
            if i < baris-1:
                file.write("\n")                    # newline ditambahkan pada file













