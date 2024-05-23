# Daftar murid di kelas
daftar_murid = ['Andika', 'Beti', 'Arif', 'Budi Wira', 'Nayo',
                'Budi Sulaiman', 'Nino', 'Nina', 'Oji', 'Ambar', 'Taqi',
                'Dila', 'Yuli', 'Indah', 'Bira']

# Menghitung jumlah nama yang mengandung kata "Budi"
budi_count = 0
nama_budi = []

for murid in daftar_murid:
    if "Budi" in murid:
        budi_count += 1
        nama_budi.append(murid)

index = 0
if budi_count >= 3:
    print("Ditemukan 3 atau lebih siswa yang namanya mengandung kata 'Budi':")
    while index < len(daftar_murid):
        print(daftar_murid[index])
        index += 1
else:
    print(f"Hanya ada {budi_count} nama Budi di kelas yaitu {', '.join(nama_budi)}")
    print("Nama siswa di kelas kecuali yang namanya mengandung kata 'Budi':")
    while index < len(daftar_murid):
        if "Budi" not in daftar_murid[index]:
            print(daftar_murid[index])
        index += 1
