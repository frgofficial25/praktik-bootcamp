# Operator Bitwise, operasi masing-masing bit

a = 9
b = 5

# Bitwise OR (|)
print('========== OR ==========')
c = a | b
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
print('------------------------- (|)')
print('nilai :',c,', binary :',format(c,'08b'))

# Bitwise AND (&)
print('\n========== AND ==========')
c = a & b
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
print('------------------------- (&)')
print('nilai :',c,', binary :',format(c,'08b'))

# Bitwise XOR (^)
print('\n========== XOR ==========')
c = a ^ b
print('nilai :',a,', binary :',format(a,'08b'))
print('nilai :',b,', binary :',format(b,'08b'))
print('------------------------- (^)')
print('nilai :',c,', binary :',format(c,'08b'))

# Bitwise NOT (~)
print('\n========== NOT ==========')
c = ~a
print('nilai :',a,', binary :',format(a,'08b'))
print('------------------------- (~)')
print('nilai :',c,', binary :',format(c,'08b'))
# Catatan: hasil NOT dipengaruhi oleh signed integer

# Cara mendapatkan hasil flipping bit murni (menggunakan XOR dengan bit 1)
print('------------------------- (^) trik flip')
d = 0b0000000011111111
e = d ^ a
print('nilai :',e,', binary :',format(e,'08b'))

# Shifting

# Shift Right (>>)
print('\n========== >> ==========')
c = a >> 2
print('nilai :',a,', binary :',format(a,'08b'))
print('------------------------- (>>)')
print('nilai :',c,', binary :',format(c,'08b'))

# Shift Left (<<)
print('\n========== << ==========')
c = a << 2
print('nilai :',a,', binary :',format(a,'08b'))
print('------------------------- (<<)')
print('nilai :',c,', binary :',format(c,'08b'))