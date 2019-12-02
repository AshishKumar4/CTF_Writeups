import subprocess

def checkStr(s):
    p = subprocess.Popen(['wine', 'inctfchall.exe'], stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    p.stdin.write(s.encode('utf-8'))
    h = p.communicate()[0].decode('utf-8').split('\r\n')[0]
    print(h)
    h = h.split('}')[-1]
    return int(h)

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#$%^&*()'

k = 'inctf{'
p = checkStr(k + '}')

for i in range(len(k),30):
    for j in symbols:
        n = checkStr(k + j + '}')
        print(n, j)
        if n > p:
            print("Found!", j)
            k += j
            p = n 
            break
