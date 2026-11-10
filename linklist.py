# Program Antrean Menggunakan LinkedList
class Node:

    def __init__(self, nama):  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
        self.nama = nama  # pyright: ignore[reportUnannotatedClassAttribute]
        self.next = None  # pyright: ignore[reportUnannotatedClassAttribute]


class AntreanLinkedList:

    def __init__(self):
        self.head = None  # pyright: ignore[reportUnannotatedClassAttribute]

    def tambah_antrean(self, nama):  # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        new_node = Node(nama)  # pyright: ignore[reportUnknownArgumentType]
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # pyright: ignore[reportAttributeAccessIssue]
        print(f"-> {nama} masuk ke dalam antrean.")

    def panggil_antrean(self):
        if not self.head:
            print("-> Antrean kosong!")
        else:
            dilepaskan = self.head.nama  # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType]
            self.head = self.head.next
            print(f"-> {dilepaskan} selesai dilayani (keluar antrean).")

    def tampilkan_antrean(self):
        print("\n--- Status Antrean ---")
        if not self.head:
            print("Tidak ada orang di antrean.")
            return

        current = self.head
        no = 1
        while current:
            print(f"{no}. {current.nama}")  # pyright: ignore[reportUnknownMemberType]
            current = current.next
            no += 1


# --- JALANKAN PROGRAM ---
antrean = AntreanLinkedList()

while True:
    print("\n=== SYSTEM ANTREAN KASIR (LINKEDLIST) ===")
    print("1. Tambah Antrean Baru")
    print("2. Panggil Antrean (Hapus Depan)")
    print("3. Lihat Daftar Antrean")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan nama pelanggan: ")
        antrean.tambah_antrean(nama)  # pyright: ignore[reportUnknownMemberType]
    elif pilihan == "2":
        antrean.panggil_antrean()
    elif pilihan == "3":
        antrean.tampilkan_antrean()
    elif pilihan == "4":
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid!")