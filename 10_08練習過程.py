# 10/08 練習

# 本日練習網站
# https://cryptopals.com/
# https://2018game.picoctf.com/problems

import codecs

##  hexadecimal to ASCII
codecs.decode("41", "hex")
# b'A'
bytes.fromhex('41').decode('utf-8')
# 'A'
print ("\x41")
# A
bytearray.fromhex("41").decode()
# 'A'
chr(int('41',16))
# 'A'

##  int(base10) to binary(base2)
bin(27)
# '0b11011'
bin(27)[2:]
# '11011'

# 0x3D (base 16) to  decimal (base 10)
int('3D',16)
# 61
