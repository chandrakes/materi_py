#setiap hasil dari operasi komparasi adalah boolean
#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2
#lebih besar dari >
print("======lebihbesar=======")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil) #harus lebih besar agar true

#kurang dari
print("======kurangdari=======")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

#lebih dari sama dengan >=
print("======lebihdarisamadengan=======")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

#kurang dari sama dengan >=
print("======kurangdarisamadengan=======")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',a,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

#sama dengan ==
print("========samadengan=======")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

#tidak sama dengan !=
print("========samadengan=======")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)


print("========objectidentity(is)=======")
#is sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 5
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

#is sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 6
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

print("========objectidentity(isnot)=======")
#is sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 5
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)

#is not sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 6
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)