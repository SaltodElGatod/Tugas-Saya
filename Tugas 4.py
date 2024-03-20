print("===== KALKULATOR MENGONVERSI NILAI =====")
masukkan_bilangan = int(input("Masukkan Angka Anda Yang Diinginkan: "))
masukkan_pilihan_user = int(input("Silahkan Pilih 1, 2, 3, atau 4: "))

def pilih_operasi(pilihan, bilangan):
    if pilihan == 1:
        print("Bilangan Biner Dari", bilangan, "Adalah", bin(bilangan)[2:])
    elif pilihan == 2:
        print("Bilangan Oktal Dari", bilangan, "Adalah", oct(bilangan)[2:])
    elif pilihan == 3:
        print("Masukkan Bilangan Desimal Dari", bilangan, "Adalah", bilangan)
    elif pilihan == 4:
        print("Bilangan Hexadesimal Dari", bilangan, "Adalah", hex(bilangan)[2:])
    else:
        print("Pilihan Tidak Sesuai")

pilih_operasi(masukkan_pilihan_user, masukkan_bilangan)