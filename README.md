# Praktikum 5
## Program Sederhana Dictionary
Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.

Mata Kuliah: Bahasa Pemograman
## Kode Program
```python

# Program Input Nilai Mahasiswa
# Menggunakan Dictionary

data_mahasiswa = {}

def tampilkan_data():
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

def tambah_data():
    print("Tambah Data")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai UTS: "))
    uts = float(input("Nilai UAS: "))
    uas = float(input("Nilai Tugas: "))
    data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas}
    print("Data berhasil ditambahkan!")

def ubah_data():
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        print("Masukkan data baru:")
        data_mahasiswa[nim]['nama'] = input("Nama: ")
        data_mahasiswa[nim]['tugas'] = float(input("Nilai UTS: "))
        data_mahasiswa[nim]['uts'] = float(input("Nilai UAS: "))
        data_mahasiswa[nim]['uas'] = float(input("Nilai Tugas: "))
        print("Data berhasil diubah!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

def hapus_data():
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

def cari_data():
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
        print("\nData Mahasiswa")
        print("="*25)
        print(f"NIM         : {nim}")
        print(f"Nama        : {data['nama']}")
        print(f"Nilai UTS   : {data['uts']:.0f}")
        print(f"Nilai UAS   : {data['uas']:.0f}")
        print(f"Nilai Tugas : {data['tugas']:.0f}")
        print(f"Nilai Akhir : {nilai_akhir:.2f}")
        print("="*25)
    else:
        print("Data dengan NIM tersebut tidak ditemukan!")

while True:
    print("\nProgram Input Nilai")
    print("====================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia.")
```
## Hasil Kode Program
![foto](https://github.com/Manueljds2311105/foto/blob/91c436c5940ff771fdb473f548f4ce3c1be9ac9f/Praktikum%205.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2011_19_2024%204_54_24%20PM.png)
![foto](https://github.com/Manueljds2311105/foto/blob/91c436c5940ff771fdb473f548f4ce3c1be9ac9f/Praktikum%205.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2011_19_2024%204_55_04%20PM.png)
![foto](https://github.com/Manueljds2311105/foto/blob/91c436c5940ff771fdb473f548f4ce3c1be9ac9f/Praktikum%205.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2011_19_2024%204_55_30%20PM.png)
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/91c436c5940ff771fdb473f548f4ce3c1be9ac9f/Praktikum%205.png)
## Penjelasan
1. Tampilkan Data (Lihat Data)
- Fungsi: Menampilkan seluruh data mahasiswa beserta nilai tugas, UTS, UAS, dan nilai akhir.
- Nilai akhir dihitung dengan rumus: Nilai Akhir=(30%×Tugas)+(35%×UTS)+(35%×UAS)
- Jika tidak ada data, akan muncul pesan bahwa data tidak tersedia.

Menggunakan perulangan while True untuk membuat menu interaktif.

2. Tambah Data
- Fungsi: Memasukkan data baru mahasiswa ke dalam dictionary data_mahasiswa.
- Data yang dimasukkan meliputi:
  
  NIM (sebagai kunci)
  
  Nama
  
  Nilai Tugas, UTS, dan UAS
3. Ubah Data
- Fungsi: Memodifikasi data mahasiswa yang sudah ada berdasarkan NIM.
- Jika NIM tidak ditemukan, Data dengan NIM tersebut tidak ditemukan!.
4. Hapus Data
- Fungsi: Menghapus data mahasiswa berdasarkan NIM.
- Jika NIM tidak ditemukan, Data dengan NIM tersebut tidak ditemukan!.
5. Cari Data
- Fungsi: Mencari data mahasiswa berdasarkan NIM.
- Menampilkan data spesifik mahasiswa, termasuk nilai akhir, jika NIM ditemukan.
6. Keluar
- Fungsi: Mengakhiri program.
