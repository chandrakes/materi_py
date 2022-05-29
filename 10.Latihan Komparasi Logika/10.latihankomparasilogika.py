#membuat gabungan area rentang dari angka

#++++++++++3----------10++++++++++++
inputuser = float(input("masukan angka yang bernilai kurang dari 3 \natau \nlebih besar dari 10\n:"))
#++++++++++++++3----------- kurang dari 3
kurangdari = (inputuser < 3)
print("Apakah kurang dari 3 = ",kurangdari)
#----------------------------10+++++++ lebih dari 10
lebihdari = (inputuser > 10)
print("Apakah lebih dari 10 = ",lebihdari)
#or
gabungan = kurangdari or lebihdari
print("Angka yang anda masukan : ",gabungan)

#kasus irisan ----------3+++++++++++10---------------
inputuser = float(input("\nmasukan angka yang bernilai lebih dari 3 \ndan \nkurang dari dari 10\n:"))
#-----------------3++++++++++ lebih dari 3
lebihdari = inputuser > 3
print("Apakah lebih dari 3 : ",lebihdari)
#++++++++++++10----------- kurang dari 10
kurangdari = inputuser < 10
print("Apakah kurang dari 10 : ",kurangdari)
#and
gabungand = kurangdari and lebihdari
print("angka yang anda masukan : ",gabungand)