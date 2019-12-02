from Crypto.Cipher import DES
import binascii

IV = '13371337'


def getNibbleLength(offset):
    if str(offset)[0] == "9":
        return len(str(offset))+1
    return len(str(offset))


def duck(aChr):
    try:
        return int(aChr)
    except:
        return "abcdef".index(aChr)+11

def encodeText(plainText, offset):
    hexEncoded = plainText.encode("hex")
    print(hexEncoded)
    nibbleLen = getNibbleLength(offset)
    print(nibbleLen)
    output = ""
    for i in range(0, len(hexEncoded), 2):
        hexByte = hexEncoded[i:i+2]
        print(hexByte)
        try:
            s1 = str(duck(hexByte[0]) + offset).rjust(nibbleLen, "0")
            output += s1
            s2 = str(duck(hexByte[1]) + offset).rjust(nibbleLen, "0")
            output += s2
            print(s1,s2)
        except Exception as e:
            print("ERROR", e)
            continue
    return output


def decodeText(cipher, offset):
    hexDecoded = cipher.decode('hex').decode('hex')
    nibbleLen = getNibbleLength(offset)
    output = ""
    for i in range(0, len(hexEncoded), 2):
        hexByte = hexEncoded[i:i+2]
        try:
            output += str(duck(hexByte[0]) + offset).rjust(nibbleLen, "0")
            output += str(duck(hexByte[1]) + offset).rjust(nibbleLen, "0")
        except:
            continue
    return output


def padInput(input):
    bS = len(input)/8
    if len(input) % 8 != 0:
        return input.ljust((bS+1)*8, "_")
    return input


def desEncrypt(input, key):
    cipher = DES.new(key, DES.MODE_OFB, IV)
    msg = cipher.encrypt(padInput(input))
    return msg


def createKey(hex, fileName):
    with open(fileName, 'wb') as f:
        f.write(binascii.unhexlify(hex))


def createChallenge():
    createKey("011F011F010E010E", "key1")
    createKey("1F011F010E010E01", "key2")
    plainText = open('FLAG.txt').read()
    key1 = open('key1').read()
    byte = desEncrypt(plainText, key1)
    key2 = open('key2').read()
    cipherText = desEncrypt(byte, key2)
    print(cipherText)


createKey("E001E001F101F101", "key1")
createKey("01E001E001F101F1", "key2")
plainText = open('DES2Bytes.txt').read()
key1 = open('key1').read()
byte = desEncrypt(plainText, key1)
key2 = open('key2').read()
cipherText = desEncrypt(byte, key2)
print(cipherText)

cipher = encodeText(binascii.hexlify(cipherText), 9133337)
f = open('test.enc', 'w')
f.write(cipher)
