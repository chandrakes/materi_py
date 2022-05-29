#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment
a = 5 #adalah assignment
print('nilai a = ',a)
a += 1#artinnya a = a + 1
print('nilai a += 1, nilai a menjadi',a)
a -= 2#artinnya a = a - 2
print('nilai a -= 2, nilai a menjadi',a)
a *= 5#artinnya a = a * 5
print('nilai a *= 5, nilai a menjadi',a)
a /= 2#artinnya a = a / 2
print('nilai a /= 2, nilai a menjadi',a)

#Modulus dan floor division
b = 10
print('\n Nilai b =',b)
b %= 3
print('nilai b %= 3, nilai b menjadi',b)
b = 10
print('\n Nilai b =',b)
b //= 3
print('nilai b //= 3, nilai b menjadi',b) 

#Pangkat/eksponen
a = 5
print('\n Nilai a =',a)
a **= 3
print('nilai a **= 3, nilai a menjadi',a)

#operasi bitwise
c = True
print('\n Nilai c =',c)
c |= False
print('nilai c |= False, nilai c menjadi',c)

c = False
print('\n Nilai c =',c)
c |= False
print('nilai c |= False, nilai c menjadi',c)

#and
c = True
print('\n Nilai c =',c)
c &= False
print('nilai c &= False, nilai c menjadi',c)

c = True
print('\n Nilai c =',c)
c &= True
print('nilai c &= True, nilai c menjadi',c)

#XOR
c = True
print('\n Nilai c =',c)
c ^= False
print('nilai c ^= False, nilai c menjadi',c)

c = True
print('\n Nilai c =',c)
c ^= True
print('nilai c ^= True, nilai c menjadi',c)

#geser-geser
d = 0b0100
print('\n Nilai d =',format(d,'04b'))
d >>= 2
print('Nilai d >>= 2, nilai d menjadi ',format(d,'04b'))
d <<= 1
print('Nilai d <<= 1, nilai d menjadi ',format(d,'04b'))