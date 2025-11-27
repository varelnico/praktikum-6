# Dictionary untuk menyimpan data mahasiswa
# Format: { "nama": {"tugas": x, "uts": y, "uas": z} }
mahasiswa = {}

# Fungsi untuk menambah data mahasiswa
def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    
    mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas
    }
    print(f"Data '{nama}' berhasil ditambahkan!\n")

# Fungsi untuk menampilkan semua data mahasiswa
def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not mahasiswa:
        print("Belum ada data.\n")
        return
    
    for nama, nilai in mahasiswa.items():
        print(f"Nama  : {nama}")
        print(f"  Tugas : {nilai['tugas']}")
        print(f"  UTS   : {nilai['uts']}")
        print(f"  UAS   : {nilai['uas']}")
        print("-" * 30)

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan!\n")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama):
    if nama in mahasiswa:
        print(f"\n=== Ubah Data Mahasiswa: {nama} ===")
        tugas = float(input("Nilai Tugas baru : "))
        uts = float(input("Nilai UTS baru   : "))
        uas = float(input("Nilai UAS baru   : "))
        
        mahasiswa[nama]["tugas"] = tugas
        mahasiswa[nama]["uts"] = uts
        mahasiswa[nama]["uas"] = uas
        print(f"Data '{nama}' berhasil diperbarui!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan!\n")

# PROGRAM UTAMA
while True:
    print("""
=== MENU PILIHAN ===
1. Tambah Data
2. Tampilkan Data
3. Ubah Data
4. Hapus Data
5. Keluar
""")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.\n")