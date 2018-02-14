from cs50 import get_int,get_string
import sys

class caesar:
    number = len(sys.argv)
    def check(self,number):
        if len(sys.argv) != number or not sys.argv[1].isdigit():
            print("invalid input ---name program key number")
            sys.exit(1)
        key = int(sys.argv[1])
        return key

    def get_plaintext(self,sentence):
        return get_string(sentence)
    def cipher(self,text,key):
        print("ciphertext: ",end="")
        for letter in text:
            if letter.isalpha():
                if letter.isupper():
                    letter = ord(letter) - 65
                    letter = (key + letter)%26
                    letter +=65
                    print(chr(letter),end="")
                elif letter.lower():
                    letter = ord(letter) - 97
                    letter = (key + letter)%26
                    letter +=97
                    print(chr(letter),end="")
            else:
                print(letter,end="")
        print()


