    # From Analysis of run.c, it was clear, The Flag is XORed with '1' and stored.
    # XOR of 'TUCTF{', which are the first few characters we know of, is 'UTBUGz'

    # Thus, just simply use 'strings' to get the string with those initials -->
        ## strings core | grep 'UTBUGz'
        ### UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|

    # XORed with 1 in python3 gives the flag 
        ##  ''.join([chr(ord(i)^1) for i in 'UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|'])
        ### 'TUCTF{c0r3_dump?_N3v3r_h34rd_0f_y0u}'