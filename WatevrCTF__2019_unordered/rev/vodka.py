def passDecoder(a):
    b = range(0, len(a))
    return ''.join([chr(i^ord(j)) for i,j in zip(b, a)])

def getAddress(base = 0x0000555555554000, offset=0):
    return hex(base + (offset&0xffff))

# Disassemble the binary, also put it in gdb and use getAddress to get address of relevant instruction
# Analyze operations instruction by instruction, function by function
# setting breakpoints at getAddress(offset=0x1297) and getAddress(offset=0x100e) reveals 
# encoded passwords in the stack. To understand the logic, just run the code in gdb with 
# other breakpoints, and eventually figure out the reverse logic as that defined in 
# passDecoder() function.

passDecoder('lnn\\}jsX|ae~kezPyeMdufIcpxnDy|mf')
# Result=> 'lol_you_thought_it_was_that_easy'
passDecoder('w`vfrw}s`=d`9Rf;sz#}sJpxjFi+vhAwABIJJB@HZZEAY\003ZJQ\\O')
# Result=> 'watevr{th4nk5_h4ck1ng_for_s0ju_hackingforsoju.team}'