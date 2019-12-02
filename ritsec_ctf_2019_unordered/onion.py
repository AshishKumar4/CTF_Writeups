import base64

def from16(l):
    return base64.b16decode(l).decode('utf-8')

def from64(l):
    return base64.b64decode(l).decode('utf-8')

def from32(l):
    return base64.b32decode(l).decode('utf-8')

f = open('onionlayerencoding.txt', 'r').read()
l = str(f)
k = ''
for i in range(0, 150):
    try:
        print(i, "Trying b16...")
        k = from16(l)
    except:
        print("Trying b32...")
        try:
            k = from32(l)
        except:
            print("Trying b64...")
            try:
                k = from64(l)
            except:
                print("Some problem...")
                print(l[:100])
    print(k[:100])
    l = k

