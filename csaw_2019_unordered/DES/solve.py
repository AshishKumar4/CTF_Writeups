def decodeText(cipher, offset):
	nibbleLen = getNibbleLength(offset)
	print(nibbleLen)
	p = ""
	for i in range(0, len(cipher), nibbleLen*2):
		try:
			k1 = int(cipher[i:i+nibbleLen]) - offset
			k2 = int(cipher[i+nibbleLen:i+(nibbleLen*2)]) - offset
			if(k1 >= 11):
				k1 = hex(k1-1)[:-1]
			else:
				k1 = str(k1)
			if(k2 >= 11):
				k2 = hex(k2-1)[:-1]
			else:
				k2 = str(k2)
			o = k1+k2 
			print(o)
			p += o
		except Exception as e:
			print("Error", e)
			pass
	print(p)
	r = p.decode('hex').decode('hex')
	print(r)
	return r

k = decodeText(open('DES2Bytes.enc').read(), 9133337)
k2 = '0x011F011F010E010E'[2:]
k1 = '0x1F011F010E010E01'[2:]
byte = desEncrypt(plainText, binascii.unhexlify(k1))
print(byte)
cipherText = desEncrypt(byte, binascii.unhexlify(k2))
print(cipherText)