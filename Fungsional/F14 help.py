# Program Help
# Fungsi yang menampilkan pedoman dalam penggunaan sistem

def help(role):
    print("="*10 + "HELP" + "="*10)
    # Sebagai admin
    if role == "admin":
        print("register - Untuk melakukan registrasi user baru")
        print("login - Untuk melakukan login ke dalam sistem")
        print("add_game_to_store - Untuk menambah game yang dijual pada toko")
        print("change_game_info - untuk mengubah data sebuah game")
        print("list_games - Untuk melihat list game yang dijual pada toko")
        print("change_game_stock - Untuk mengubah stok suatu game")
        print("search_games - Untuk mencari games dari toko berdasarkan ID, nama, harga, kategori, dan tahun rilis")
        print("top_up - Untuk menambahkan saldo user")
        print("help - Untuk memperlihatkan panduan penggunaan sistem")
        print("save - Untuk menyimpan data game ke dalam folder penyimpanan")

    # Sebagai user
    elif role == "user":
        print("register - Untuk melakukan registrasi user baru")
        print("login - Untuk melakukan login ke dalam sistem")
        print("listi_games - Untuk melihat list game yang dijual pada toko")
        print("buy_games - Untuk membeli game")
        print("see_owned_games - Untuk melihat games yang dimiliki")
        print("search_owned_games - Untuk mencari games yang dimiliki berdasarkan ID dan tahun rilisnya")
        print("search_store - Untuk mencari games dari toko berdasarkan ID, nama, harga, kategori, dan tahun rilis")
        print("top_up - Untuk menambahkan saldo user")
        print("receipts - Untuk melihat riwayat pembelian games")
        print("load - Untuk meload data game ke dalam sistem")
        print("save - Untuk menyimpan data game ke dalam folder penyimpanan")
        print("exit - Untuk keluar dari sistem aplikasi")
        print("help - Untuk memperlihatkan panduan penggunaan sistem")