# Program Input Nilai Mahasiswa
# Menggunakan Dictionary

data_mahasiswa = {}

while True:
    menu = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    if menu.lower() == 'l':
        if data_mahasiswa:
            print("\nDaftar Nilai")
            print("="*61)
            print("| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS |  AKHIR  |")
            print("="*61)
            no = 1
            for nim, data in data_mahasiswa.items():
                nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
                print(f"| {no:<2} | {nim:<8} | {data['nama']:<10} | {data['tugas']:<5.0f} | {data['uts']:<3.0f} | {data['uas']:<3.0f} | {nilai_akhir:<7.2f} |")
                no += 1
            print("="*61)
        else:
            print("\nDaftar Nilai")
            print("="*61)
            print("| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS |  AKHIR  |")
            print("="*61)
            print("|                      TIDAK ADA DATA                       |")
            print("="*61)

    elif menu.lower() == 't':
        print("Tambah Data")
        nim = input("NIM: ")
        nama = input("Nama: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas}
        print("Data berhasil ditambahkan!")

    elif menu.lower() == 'u':
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            print("Masukkan data baru:")
            data_mahasiswa[nim]['nama'] = input("Nama: ")
            data_mahasiswa[nim]['tugas'] = float(input("Nilai Tugas: "))
            data_mahasiswa[nim]['uts'] = float(input("Nilai UTS: "))
            data_mahasiswa[nim]['uas'] = float(input("Nilai UAS: "))
            print("Data berhasil diubah!")
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'h':
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'c':
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            data = data_mahasiswa[nim]
            nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
            print("\nData Mahasiswa")
            print("="*25)
            print(f"NIM         : {nim}")
            print(f"Nama        : {data['nama']}")
            print(f"Nilai Tugas : {data['tugas']:.0f}")
            print(f"Nilai UTS   : {data['uts']:.0f}")
            print(f"Nilai UAS   : {data['uas']:.0f}")
            print(f"Nilai Akhir : {nilai_akhir:.2f}")
            print("="*25)
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'k':
        break

    else:
        print("Pilih menu yang tersedia")
