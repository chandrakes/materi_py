data = 'ini adalah string'
print(data)
print(type(data))

#1.cara membuat string
'''
    1.dengan single quote '...'
    2.dengan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)

print('"halo apa kabar"')
print("'halo apa kabar'")
print("ini adalah hari jum'at")

#2.membuat tanda \

#membuat tanda ' menjadi string
print('mari salat jum\'at')
print('g\'day isn\'t it?')

#backlash
print("C:\\user\\chanchan")

#tab
print("ucup\t\t\ otong semakin jauh")

#backspace
print("ucup \botong, jadi deketan")

#newline
print("ini baris pertama \n ini baris kedua\n ini baris ketiga") #LF > Line feed > unix, macos, linux
print("baris pertama \r baris kedua") # CR > Carriage return > commodore, acorn, lisp
print("baris pertama \r\n baris kedua") #CRLF > Line feed carriage return > dipakai oleh windows

#3.string literal/raw

#hati-hati
print('C:\new folder') #akan salah path nya

#menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print("""
Nama : chan
Kelas: 3 sma
""")

#multiline literal string dan RAW
print(r"""
Nama : chan
Kelas: 3 sma
Website : www.chanchan.com/newid
""")