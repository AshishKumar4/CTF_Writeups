from struct import *

clean = lambda x : x.split('\n')[1:-2]
pad = lambda x : x + '\00'*(8-len(x))

kk = clean(open('yy', 'rb').read())
l = [unpack('q', pad(i))[0] for i in kk]
for i in l:
    print(hex(i))

print("\n\nOffset ==>")
o = l[0] - l[1]
print(hex(o))

system_offset = 0x045390
execve_offset = 0x0cc870
puts_offset = 0x06f690

libc = l[0] - puts_offset
print("\nLibc offset: ", hex(libc))

print("\nAll Offsets...")
all_offsets = [i - libc for i in l]
for i in all_offsets:
    print(hex(i))