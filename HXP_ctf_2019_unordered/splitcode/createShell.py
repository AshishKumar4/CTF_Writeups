from pwn import *

clear_reg : lambda reg: ('shl ' + reg + ';')*16

def move_val(reg, val):
    
