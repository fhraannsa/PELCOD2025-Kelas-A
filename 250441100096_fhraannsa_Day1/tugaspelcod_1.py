episode = 10
waktu = 35
total_durasi = episode * waktu
jam = total_durasi // 60
menit = total_durasi % 60
print("total_duras:" , jam, "jam" , menit, "menit:")
print("="*50)


cupang = int(input("Masukkan Cupang : "))
koi = int(input("Masukkan koi : "))
beli_cupang = int(input("Masukkan beli cupang : "))
beli_koi = int(input("Masukkan beli koi : "))
uang_yang_dibawa =068.000+100
penghitungan_cupang = cupang * beli_cupang
penghitungan_koi = koi * beli_koi
total_belanja = penghitungan_cupang+penghitungan_koi
sisa_uang = uang_yang_dibawa-total_belanja 
print("total belanja:" , f"Rp {total_belanja:,}")
print("sisa_uang:" ,f"Rp {sisa_uang:,}")
print("="*50) 



perjalanan = int(input("Masukkan 3 angka terakhir NIM : "))
nim_1 = int(input("Masukkan 1 angka terakhir NIM : "))
jarak = perjalanan
konsumsi_BBM = 2.7
kapasitas = nim_1 + 3
harga_perliter = 1690 + perjalanan

total_bensin = jarak / konsumsi_BBM
if total_bensin > 3:
 harga_perliter-= 500
total_biaya = total_bensin * harga_perliter
dikali_isi = int(total_bensin // kapasitas)
if total_bensin % kapasitas:
 dikali_isi += 1
 
 print("===hasil===")
 print("total jarak:", jarak, "km")
 print("total bensin yang dibutuhkan:", round(total_bensin, 2),"liter")
 print("harga bensin perliter:",harga_perliter)
 print("total biaya bensin:", round(total_biaya, 2))
 print("kali isi bensin:", dikali_isi)
