# Program Help
# Fungsi yang menampilkan pedoman dalam penggunaan sistem

def help(role):
    print("="*10 + "HELP" + "="*10)
    # Sebagai admin
    if role == "admin":
        print("register - Untuk melakukan registrasi user baru")
        print("login - Untuk melakukan login ke dalam sistem")
        print("tambahGame - Untuk menambah game yang dijual pada toko")
        print("ubahGame - untuk mengubah data sebuah game")
        print("listingGame - Untuk melihat list game yang dijual pada toko")
        print("ubahStok - Untuk mengubah stok suatu game")
        print("cariGameStore - Untuk mencari games dari toko berdasarkan ID, nama, harga, kategori, dan tahun rilis")
        print("exit - Untuk keluar dari sistem aplikasi")
        print("help - Untuk memperlihatkan panduan penggunaan sistem")

    # Sebagai user
    elif role == "user":
        print("register - Untuk melakukan registrasi user baru")
        print("login - Untuk melakukan login ke dalam sistem")
        print("listingGame - Untuk melihat list game yang dijual pada toko")
        print("beliGame - Untuk membeli game")
        print("lihatOwnedGames - Untuk melihat games yang dimiliki")
        print("cariOwnedGames - Untuk mencari games yang dimiliki berdasarkan ID dan tahun rilisnya")
        print("cariGameStore - Untuk mencari games dari toko berdasarkan ID, nama, harga, kategori, dan tahun rilis")
        print("topUpSaldo - Untuk menambahkan saldo user")
        print("lihatRiwayat - Untuk melihat riwayat games yang telah dibeli")
        print("load - Untuk meload data game ke dalam sistem")
        print("save - Untuk menyimpan data game ke dalam folder penyimpanan")
        print("exit - Untuk keluar dari sistem aplikasi")
        print("help - Untuk memperlihatkan panduan penggunaan sistem")