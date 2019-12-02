def cracker(b):
    for i in range(0, 255):
        if y(i) == b:
            print('candidate', hex(i), chr(i))
            if chr(i) not in j:
                print("Solution Found! ", i, chr(i))
