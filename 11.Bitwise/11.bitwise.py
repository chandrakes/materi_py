#operator bitwise, operasi biner, binary
a = 9
b = 5

#bitwise OR (|)
c = a|b
print('\n ==============OR==============')
print('Nilai :',a,'binary :',format(a,'08b'))
print('Nilai :',b,'binary :',format(b,'08b'))
print('  ------------------------------(|)')
print('Nilai :',c,'binary :',format(c,'08b'))

#bitwise AND (&)
c = a&b
print('\n ==============AND==============')
print('Nilai :',a,'binary :',format(a,'08b'))
print('Nilai :',b,'binary :',format(b,'08b'))
print('  ------------------------------(|)')
print('Nilai :',c,'binary :',format(c,'08b'))

#bitwise XOR (^)
c = a^b
print('\n ==============XOR==============')
print('Nilai :',a,'binary :',format(a,'08b'))
print('Nilai :',b,'binary :',format(b,'08b'))
print('  ------------------------------(|)')
print('Nilai :',c,'binary :',format(c,'08b'))

#bitwise NOT(~)
c = ~a
print('\n ==============NOT==============')
print('Nilai :',a,'binary :',format(a,'08b'))
print('  ------------------------------(|)')
print('Nilai :',c,'binary :',format(c,'08b'))
