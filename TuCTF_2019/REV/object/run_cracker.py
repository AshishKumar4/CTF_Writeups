import subprocess

def checkStrBetter(s, tot_len = 44):
    s = s + (tot_len - len(s))*'a'
    p = subprocess.getoutput("echo '" + s + "' | ./run")
    #print(p)
    h = p.split('\n')[-1]
    #print(h)
    h = h.split(' ')[-1]
    return int(h)

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-!@#$%^&*()'

k = 'TUCTF{'
p = checkStrBetter(k)

for i in range(len(k),44):
    for j in symbols:
        n = checkStrBetter(k + j)
        #print(n, j)
        if n > p:
            print("Found!", j)
            k += j
            p = n 
            break

print(''.join(k) + '}')
