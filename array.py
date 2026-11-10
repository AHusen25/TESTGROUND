# Program Data Mahasiswa Menggunakan Array (List)
daftar_mahasiswa = []


def tampilkan_menu():
    print("\n=== MENU DATA MAHASISWA (ARRAY) ===")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Semua Mahasiswa")
    print("3. Edit Nama Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")


while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        daftar_mahasiswa.append(nama)  # pyright: ignore[reportUnknownMemberType]
        print(f"-> {nama} berhasil ditambahkan!")

    elif pilihan == "2":
        print("\n--- Daftar Mahasiswa ---")
        if not daftar_mahasiswa:
            print("Data masih kosong.")
        else:
            for index, nama in enumerate(daftar_mahasiswa):  # pyright: ignore[reportUnknownVariableType, reportUnknownArgumentType]
                print(f"{index + 1}. {nama}")

    elif pilihan == "3":
        if not daftar_mahasiswa:
            print("Data kosong, tidak ada yang bisa di-edit.")
        else:
            no = int(input("Masukkan nomor mahasiswa yang mau di-edit: ")) - 1
            if 0 <= no < len(daftar_mahasiswa):  # pyright: ignore[reportUnknownArgumentType]
                nama_baru = input("Masukkan nama baru: ")
                daftar_mahasiswa[no] = nama_baru
                print("-> Data berhasil diubah!")
            else:
                print("Nomor tidak ditemukan!")

    elif pilihan == "4":
        if not daftar_mahasiswa:
            print("Data kosong, tidak ada yang bisa dihapus.")
        else:
            no = int(input("Masukkan nomor mahasiswa yang mau dihapus: ")) - 1
            if 0 <= no < len(daftar_mahasiswa):  # pyright: ignore[reportUnknownArgumentType]
                dihapus = daftar_mahasiswa.pop(no)  # pyright: ignore[reportUnknownVariableType]
                print(f"-> {dihapus} berhasil dihapus!")
            else:
                print("Nomor tidak ditemukan!")

    elif pilihan == "5":
        print("Selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")