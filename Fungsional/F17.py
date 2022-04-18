from F16 import *

def exit(a):
    # Jika inputan tidak valid
    # Maka program akan menanyakan ulang. Di mana input harus berlaku untuk Y atau N dalam huruf kecil maupun besar.
    while (a != "y") and (a != "Y") and (a != "n") and (a != "N"):
        print()
        print("input harus berupa Y, N, y, atau n")
        a = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    
    # Menjalankan prosedur save dan program selesai
    if (a.lower() == "y") :
        save()
        print("Telah disimpan, program selesai.")

    # Program selesai dan tidak menyimpan data pada file 
    elif (a.lower() == "n") : 
        print("Tidak disimpan, program selesai.")

a = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
exit(a)
