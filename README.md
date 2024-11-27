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

while True:
    menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")

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
        print()
        print("Tambah Data")
        nim = input("NIM: ")
        nama = input("Nama: ")
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas}

    elif menu.lower() == 'u':
        print()
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            print("Masukkan data baru:")
            data_mahasiswa[nim]['nama'] = input("Nama: ")
            data_mahasiswa[nim]['uts'] = float(input("Nilai UTS: "))
            data_mahasiswa[nim]['uas'] = float(input("Nilai UAS: "))
            data_mahasiswa[nim]['tugas'] = float(input("Nilai Tugas: "))
            print("Data berhasil diubah!")
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'h':
        print()
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'c':
        print()
        nim = input("NIM: ")
        if nim in data_mahasiswa:
            data = data_mahasiswa[nim]
            nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
            print("\nData Mahasiswa")
            print("="*24)
            print(f"NIM         : {nim}")
            print(f"Nama        : {data['nama']}")
            print(f"Nilai UTS   : {data['uts']:.0f}")
            print(f"Nilai UAS   : {data['uas']:.0f}")
            print(f"Nilai Tugas : {data['tugas']:.0f}")
            print(f"Nilai Akhir : {nilai_akhir:.2f}")
            print("="*24)
        else:
            print(f"Data dengan NIM {nim} tidak ditemukan!")

    elif menu.lower() == 'k':
        break
    else:
        print()
        print("Pilihan Tidak Valid")
```
## Hasil Kode Program
![foto](https://github.com/Manueljds2311105/foto/blob/69288e90ff5b730990a80215adcb2f0b0c0835ad/Praktikum%205.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2011_27_2024%209_15_35%20AM.png)
## flowchart
![foto](https://github.com/Manueljds2311105/foto/blob/91c436c5940ff771fdb473f548f4ce3c1be9ac9f/Praktikum%205.png)
## Penjelasan
```python
data_mahasiswa = {}
```
- Fungsi: Membuat dictionary kosong bernama data_mahasiswa untuk menyimpan data mahasiswa.
- Struktur Data:

  Kunci (key): NIM mahasiswa.
  
  Nilai (value): Dictionary berisi nama mahasiswa dan nilai tugas, UTS, serta UAS.
```python
while True:
    menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
```
- Fungsi: Menjalankan perulangan tak terbatas untuk menampilkan menu pilihan.
- Input: Mengambil pilihan pengguna untuk menentukan tindakan.
- menu.lower(): Mengonversi input menjadi huruf kecil agar input tidak case-sensitive.
```python
if menu.lower() == 'l':
    if data_mahasiswa:
```
- Fungsi: Mengecek apakah ada data dalam data_mahasiswa.
- Kasus 1: Jika data ada, tampilkan tabel nilai mahasiswa.
- Kasus 2: Jika kosong, tampilkan pesan "TIDAK ADA DATA".
```python
print("\nDaftar Nilai")
print("="*61)
print("| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS |  AKHIR  |")
print("="*61)
no = 1
for nim, data in data_mahasiswa.items():
    nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
    print(f"| {no:<2} | {nim:<8} | {data['nama']:<10} | {data['tugas']:<5.0f} | {data['uts']:<3.0f} | {data['uas']:<3.0f} | {nilai_akhir:<7.2f} |")
    no += 1
```
- Fungsi: Membuat header tabel yang rapi menggunakan karakter | dan =.
- Fungsi:
  - Iterasi semua data dalam data_mahasiswa.
  - Menghitung nilai akhir dengan bobot:
    30% untuk tugas.
    35% untuk UTS.
    35% untuk UAS.
  - Menampilkan data secara berformat dengan f-string.
  - no adalah nomor urut.
  ```python
  elif menu.lower() == 't':
    print()
    print("Tambah Data")
    nim = input("NIM: ")
    nama = input("Nama: ")
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    tugas = float(input("Nilai Tugas: "))
    data_mahasiswa[nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas}
  ```
- Meminta input pengguna untuk NIM, nama, dan nilai.
- Nilai UTS, UAS, dan Tugas diubah ke tipe float.
- Menambahkan data ke dictionary data_mahasiswa dengan NIM sebagai kunci.
```python
elif menu.lower() == 'u':
    print()
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        print("Masukkan data baru:")
        data_mahasiswa[nim]['nama'] = input("Nama: ")
        data_mahasiswa[nim]['uts'] = float(input("Nilai UTS: "))
        data_mahasiswa[nim]['uas'] = float(input("Nilai UAS: "))
        data_mahasiswa[nim]['tugas'] = float(input("Nilai Tugas: "))
        print("Data berhasil diubah!")
    else:
        print(f"Data dengan NIM {nim} tidak ditemukan!")
```
- Meminta NIM.
- Jika NIM ada di data_mahasiswa, data lama diperbarui dengan data baru.
- Jika NIM tidak ditemukan, tampilkan pesan error.
```python
elif menu.lower() == 'h':
    print()
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data berhasil dihapus!")
    else:
        print(f"Data dengan NIM {nim} tidak ditemukan!")
```
- Meminta NIM
- Jika NIM ditemukan, data dihapus menggunakan del.
- Jika NIM tidak ditemukan, tampilkan pesan error.
```python
elif menu.lower() == 'c':
    print()
    nim = input("NIM: ")
    if nim in data_mahasiswa:
        data = data_mahasiswa[nim]
        nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
        print("\nData Mahasiswa")
        print("="*24)
        print(f"NIM         : {nim}")
        print(f"Nama        : {data['nama']}")
        print(f"Nilai UTS   : {data['uts']:.0f}")
        print(f"Nilai UAS   : {data['uas']:.0f}")
        print(f"Nilai Tugas : {data['tugas']:.0f}")
        print(f"Nilai Akhir : {nilai_akhir:.2f}")
        print("="*24)
    else:
        print(f"Data dengan NIM {nim} tidak ditemukan!")
```
- Fungsi:
  
  Meminta NIM.
  
  Jika NIM ada Menampilkan data mahasiswa dan nilai akhir.
  
  Jika tidak, tampilkan pesan error.
```python
elif menu.lower() == 'k':
    break
else:
    print()
    print("Pilihan Tidak Valid")
```
- Fungsi: Menghentikan perulangan dengan break.
- Menangani input menu yang tidak valid.
