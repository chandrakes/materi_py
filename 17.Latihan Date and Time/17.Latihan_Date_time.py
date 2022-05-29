#date and time (latihan)
import datetime as dt

print('Silahkan masukan tanggal dan bulan lahir anda')
tanggal = int(input('Tanggal \t: '))
bulan = int(input('Bulan \t\t: '))
tahun = int(input('Tahun \t\t: '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f'\nTanngal lahir Anda\t: {tanggal_lahir}')
print(f'Hari nya adalah\t\t: {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'Hari ini adalah\t\t: {hari_ini}')
umur = hari_ini - tanggal_lahir
umur_bulan = (umur.days % 365)//30
print(f'Umur Anda adalah\t: {umur.days//365} Tahun {umur_bulan} Bulan')
