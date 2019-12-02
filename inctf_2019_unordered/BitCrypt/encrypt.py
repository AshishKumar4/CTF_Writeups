from Crypto.Util.number import *
import random
from s3cr3t import flag, pub_key

def encrypt(m,pub_key):
	c = []
	bin_msg = bin(bytes_to_long(m))[2:]
	n,y = pub_key
	for i in bin_msg:
		x = random.getrandbits(100)
		if (i == '1'):
			c.append((y*pow(x,3,n))%n)
		else:
			c.append(pow(x,3,n))
	return c

ciphertext = encrypt(flag,pub_key)
f = open('ciphertext.txt','w')
f.write(str(ciphertext))
