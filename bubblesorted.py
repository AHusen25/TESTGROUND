def bubble_sort(arr, mode="asc"):  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    n = len(arr)  # pyright: ignore[reportUnknownArgumentType]

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            # Kondisi Ascending (Terkecil -> Terbesar)
            if mode == "asc" and arr[j] > arr[j + 1] or mode == "desc" and arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Jika tidak ada yang ditukar, array sudah rapi
        if not swapped:
            break

    return arr  # pyright: ignore[reportUnknownVariableType]


# --- PROGRAM INTERAKTIF ---
print("=== PROGRAM BUBBLE SORT (ASC/DESC) ===")

input_user = input(
    "Masukkan angka acak (pisahkan spasi, contoh: 40 10 50 20): "
)
angka_list = [int(x) for x in input_user.split()]

print("\nPilih Mode Pengurutan:")
print("1. Ascending (Terkecil ke Terbesar)")
print("2. Descending (Terbesar ke Terkecil)")
pilihan = input("Pilihan (1/2): ")

print(f"\nData Awal: {angka_list}")

if pilihan == "1":
    hasil = bubble_sort(angka_list.copy(), mode="asc")
    print(f"Hasil (Ascending)  : {hasil}")
elif pilihan == "2":
    hasil = bubble_sort(angka_list.copy(), mode="desc")
    print(f"Hasil (Descending) : {hasil}")
else:
    print("Pilihan tidak valid!")