print("TGL TRANS     = -")
print("NO KONTRAK    = -")
print("NO TANDA TERIMA = -")

print("Nama Konsumen = Burhan")
print("No. HP        = -")
print("Periode bayar = 18")
print("Tgl Jatuh temp= SETIAP TANGGAL 19-NOVEMBER-2021")

print("JENIS         = ADIRA FINANCE")
print("NOMOR         = EA3183DF")

tagihan = int(input("Masukkan tagihan anda = "))
admin = 7500
total = tagihan + admin
print("TOTAL BAYAR   = "+ str(total))

print("DETAIL BAYAR")
print("TOTAL BAYAR   = "+ str(total))
print("TOTAL DISKON  = 0 ")
print("SETELAH DISKON= "+ str(total))
uang = int(input("Masukkan uang anda = "))

kembali = uang - total

print("Kembalian anda= " + str(kembali))

print("terimakasih")