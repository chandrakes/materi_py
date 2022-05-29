# Width and Multiline

# Data

nama = "Chanchan"
umur = 20
tinggi = 170.1
nomsepatu = 44

# string standard
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, sepatu = {nomsepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {nama}, \nnumur = {umur}, \ntinggi = {tinggi}, \nsepatu = {nomsepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""nama = {nama}
umur = {umur}
tinggi = {tinggi}
sepatu = {nomsepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
nama = "Chanchan"
tinggi = 105.17
data_string = f"""
nama   = {nama:<5}
umur   = {umur:<5}
tinggi = {tinggi:<5}
sepatu = {nomsepatu:<5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)