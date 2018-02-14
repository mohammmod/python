import cs50
import sys


def main():
    place = []
    key = sys.argv[1]
    if len(sys.argv)>2:
        print("python3 vigenere.py keyword",end="")
        sys.exit(1)
    for letter in key:
        if not letter.isalpha():
            print("python3 vigenere.py keyword",end="")
            sys.exit(1)
    index = 0
    plaintext = cs50.get_string("plaintext: ")
    print("ciphertext: ",end="")
    for index in range(len(plaintext)):
        TakingCareOfCiphering(index,plaintext,key)
    print()

def TakingCareOfCiphering(index,plaintext,key):
        newindex = index % len(key)
        if plaintext[index].isalpha():
            TakingCareOfCapitalLetter(index,plaintext,key,newindex)
            TakingCareOfCipherSmallLetter(index,plaintext,key,newindex)
        else:
            print(plaintext[index],end="")


def TakingCareOfCapitalLetter(index,plaintext,key,newindex):
    if plaintext[index].isupper():
        if key[newindex].isupper():
            asciiletter = (((ord(plaintext[index]) - 65 ) + (ord (key[newindex]) - 65))%26)
            print(chr(asciiletter + 65),end="")
        elif key[newindex].islower():
            asciiletter = (((ord(plaintext[index]) - 65 ) + (ord (key[newindex]) - 97))%26)
            print(chr(asciiletter + 65),end="")


def TakingCareOfCipherSmallLetter(index,plaintext,key,newindex):
    if plaintext[index].islower():
        if key[newindex].isupper():
            asciiletter = (((ord(plaintext[index]) - 97 ) + (ord (key[newindex]) - 65))%26)
            print(chr(asciiletter + 97),end="")
        elif key[newindex].islower():
            asciiletter = (((ord(plaintext[index]) - 97 ) + (ord (key[newindex]) - 97))%26)
            print(chr(asciiletter + 97),end="")


if __name__=="__main__":
    main()