int main()
{
    int naddr = mmap(0x0, 0x1000, 0x3); // 0x7ffff7ffb000
    int maddr = mmap(0x0, 0x1000, 0x3); // 0x7ffff7fc9000
    int fd = open("/dev/urandom", 0, 0);
    read(fd, naddr, 0x1000);
    close(fd);
    int paddr = mmap(0xbddf000, 0x1000, 0x3);
    read(0, naddr+0x90, 0x2a); // User input 
    memset(0x7ffff7fc9000, 0xf4, 0x1000); 
    *(0x7ffff7fc9000) = 0x5d5b5a5958fc8948;
    *(0x7ffff7fc9008) = 0x5a41594158415f5e;
    *(0x7ffff7fc9010) = 0x5e415d415c415b41;
    *(0x7ffff7fc9018) = 0xf4f402eb5c9d5f41;


    *(0x7ffff7fc9020) = user_input_2bytes;

    /* does something */
    mmprotect(maddr, 0x1000, 5, 0x15);
    maddr();
    // in maddr, rsp = naddr
}