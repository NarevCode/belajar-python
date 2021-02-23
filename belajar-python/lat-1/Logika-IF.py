# KONDISI IF adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE
nilai = 9
#jika kondisi benar/TRUE maka program akan mengeksekusi program di bawah ini
if(nilai > 7):
    print("Sembilan lebih besar dari angka tujuh") #kondisi benr dieksekusi

#jika kondisi salah/False maka program tidakakan mengekskusi prnth di bawah ini
if(nilai > 10):
    print("Sembilan lebih besar dari angka sepuluh") #kondisi salah, maka tidak tereksekusi


# KONDISI IF ELSE
nilai = 3
#jika pernyataan pada if bernilai TRUE maka if akan dieksekusi. tetapi jika FALSE kode pada else yang akan dieksekusi
if(nilai > 7):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")

# KONDISI Elif
hari_ini = "Minggu"

if(hari_ini == "Selasa"):
    print("Saya akan Sekolah")
elif(hari_ini == "Rabu"):
    print("saya akan sekolah")
elif(hari_ini == "Kamis"):
    print("saya akan sekolah")
elif(hari_ini == "Jumat"):
    print("saya akan sekolah")
elif(hari_ini == "Minggu"):
    print("saya akan libur ")
    