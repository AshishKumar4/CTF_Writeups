import random
from hashlib import *
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

while True:
    a = randomString()
    h = md5(sha1(a.encode('utf-8')).hexdigest().encode('utf-8')).hexdigest()
    if 'f1a9' in h:
        print("Found!!! ", a)
    
# KAF{Dn4k_f1a9z___much_f1a9_l0t5_h4ppy}