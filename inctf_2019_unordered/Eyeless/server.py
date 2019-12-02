#!/usr/bin/env python2
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from gmpy2 import *
from secret import d, e, n
from enc_flag import enc_flag
import sys



welcome = '''
***************************************************************************************************************
*  Here are your options:                                                                            *
*                                     _  _   _  ___   _____  ___           _____  _   _  _____  _      ___    *
*       [1] Sign                     (_)( ) ( )(  _`\(_   _)(  _`\        (  _  )( ) ( )(  _  )( )    (  _`\  *
*       [2] Verify                   | || `\| || ( (_) | |  | (_(_)______ | ( ) || | | || (_) || |    | (_(_) *
*       [3] Exit                     | || , ` || |  _  | |  |  _) (______)| | | || | | ||  _  || |  _ `\__ \  *
*                                    | || |`\ || (_( ) | |  | |           | (('\|| (_) || | | || |_( )( )_) | *
*                                    (_)(_) (_)(____/' (_)  (_)           (___\_)(_____)(_) (_)(____/'`\____) *
*                                                                                                             *
***************************************************************************************************************'''


class RSA:
    def __init__(self, e, d, n):
        self.e = e
        self.d = d
        self.n = n

    def sign(self, message):
        assert message != enc_flag
        return pow(message, self.d, self.n)

    def verify(self, signature, message):
        verify = pow(signature, self.e, self.n)
        return message == verify

def main():

    rsa = RSA(e,d,n)
    print(welcome)
    while True:
        try:
            x = int(raw_input('Your choice: '))
            assert x in [1,2,3]
        except:
            print 'Invalid choice'
            sys.exit()

        if x is 1:
            try:
                message = int(raw_input('Enter the message to sign(int): '))
                print rsa.sign(message)
            except:
                print 'Invalid message'
                sys.exit()
        elif x is 2:
            try:
                sign = int(raw_input('Enter the signature to verify(int): '))

                message = int(raw_input('Message to verify(int): '))

                if rsa.verify(long(sign),message):
                    print 'Verified'
                else:
                    print 'Not verified'

            except:
                print 'Can\'t verify'
                sys.exit()

        elif x is 3:
            sys.exit()


if __name__ == '__main__':
    main()
