#!/usr/bin/env python3
import os, signal

def Speck(key, blk):
    assert tuple(map(len, (key, blk))) == (9,6)
    S = lambda j,v: (v << j | (v&0xffffff) >> 24-j)
    ws = blk[:3],blk[3:], key[:3],key[3:6],key[6:]
    x,y, l1,l0,k0 = (int.from_bytes(w,'big') for w in ws)
    print(x,y,l1,l0,k0)
    l, k = [l0,l1], [k0]
    for i in range(21):
        l.append(S(16,l[i]) + k[i] ^ i)
        k.append(S( 3,k[i])        ^ l[-1]) 
    print("==>>", x,y)
    for i in range(22):
        # print(x,y)
        x = S(16,x) + y ^ k[i]
        y = S( 3,y)     ^ x
    x,y = (z&0xffffff for z in (x,y))
    print([z.to_bytes(3,'big') for z in (x,y)])
    return b''.join(z.to_bytes(3,'big') for z in (x,y))

def test(k):
    S = lambda j,v: (v << j | (v&0xffffff) >> 24-j)
    x,y = 0, 0
    for i in range(22):
        print(x,y)
        x = (S(16,x) + y) ^ k[i]
        y = S( 3,y)     ^ x
        # k.append()
    print(x, y)
    x,y = (z&0xffffff for z in (x,y))
    return x, y
    # print([z.to_bytes(3,'big') for z in (x,y)])
    # return b''.join(z.to_bytes(3,'big') for z in (x,y))

# x = 0, y = 0
# x = k[0], y = k[0]
# x = (S(16, K[0]) + k[0])^k[1], y = S(3, k[0]) ^ ((S(16, K[0]) + k[0])^k[1]) = 
# 


def genKey(key):
    S = lambda j,v: (v << j | (v&0xffffff) >> 24-j)
    ws = key[:3],key[3:6],key[6:]
    l1,l0,k0 = (int.from_bytes(w,'big') for w in ws)
    print(l1,l0,k0)
    l, k = [l0,l1], [k0]
    for i in range(21):
        l.append(S(16,l[i]) + k[i] ^ i)
        k.append(S( 3,k[i])        ^ l[-1])
    return k

# did I implement this correctly?
assert Speck(*map(bytes.fromhex, ('1211100a0908020100', '20796c6c6172'))) == b'\xc0\x49\xa5\x38\x5a\xdc'

def antiSpeck(inp, key):
    keys = genKey(key)
    x,y = int.from_bytes(inp[:3],'big'), int.from_bytes(inp[3:],'big')
    antiS = lambda j,x: ((x&((1<<j)-1)) << (24-j)) | ((x >> j) & ((1<<(24-j))-1) )
    antiS_alter = lambda j,x: (x >> j)#&0xffffff
    for i in range(22):
        # print(x&0xffffff,y&0xffffff)
        y = antiS(3, (x^y)) 
        x = antiS(16, (x^keys[21-i]) - y)
    ws = key[:3],key[3:6],key[6:]
    l1,l0,k0 = (int.from_bytes(w,'big') for w in ws)
    l, k = [l0,l1], [k0]
    antiInt = lambda x : x.to_bytes(3, 'big')
    x,y, l1,l0,k0 = antiInt(x), antiInt(y), antiInt(l1), antiInt(l0), antiInt(k0)
    blk = x + y
    key = l1 + l0 + k0
    return key, blk

def antiSpeck_key(blk):
    x,y = int.from_bytes(blk[:3],'big'), int.from_bytes(blk[3:],'big')
    antiS = lambda j,x: ((x&((1<<j)-1)) << (24-j)) | ((x >> j) & ((1<<(24-j))-1) )
    antiS_alter = lambda j,x: (x >> j)#&0xffffff
    for i in range(22):
        # print(x&0xffffff,y&0xffffff)
        y = antiS(3, (x^y)) 
        x = antiS(16, (x^keys[21-i]) - y)
    assert x == 0 and y == 0    # Should be 0



def revH(h):
    k9 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x09'
    k, b = antiSpeck(h, k9)
    # then, h = Speck(k, b)
    assert k == k9
    # This time We know the blk == 6 x \x00, but not the key
    k = antiSpeck_key(b)

def H(m):
    s = bytes(6)
    v = m + bytes(-len(m) % 9) + len(m).to_bytes(9,'big')
    print(v)
    for i in range(0,len(v),9):
        s = Speck(v[i:i+9], s)
        print('->', s.hex())
    return s


signal.alarm(100)

h = os.urandom(6)
print(h.hex())

s = bytes.fromhex(input())
if H(s) == h:
    print('The flag is: {}'.format(open('flag.txt').read().strip()))
else:
    print('Nope.')

 