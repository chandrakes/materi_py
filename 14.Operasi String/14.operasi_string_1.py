#operasi dan manipulasi string

#1.menyambung string (concatenate)
nama_pertama = "chan"
nama_tengah = "chi"
nama_akhir = "men"
nama_lengkap = nama_pertama + " " + nama_tengah + " " +  nama_akhir
print(nama_lengkap)

#2.menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

#3.operator untuk string
#mengecek apakah ada komponen char atau string di string
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))
c = "chan"
status = c in nama_lengkap
print("string " + c + " ada di " + nama_lengkap + " = " + str(status))

#mengulang string
print("wk"*10)
print(10*"wk")

#indexing
print('index ke-0 : ' + nama_lengkap[0])
print('index ke-1 : ' + nama_lengkap[1])
print('indes ke-(-1) : ' + nama_lengkap[-1]) #diambil dari belakang
print('index ke-[0:3] : ' + nama_lengkap[0:4]) # (:) = sampai 

#item paling kecil
print("paling kecil : " + min(nama_lengkap))
#item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("character untuk ASCII 117 adalah : " + chr(data))

#4.operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))