from cs50 import get_string
import sys

plasse =[]

class Get:
    def TheKey(self,number):
        return sys.argv[number]

    def ThePlainText(self,message):
        return get_string(message)
class examiner:
    def check_(self,word):
        for letter in word:
            if not letter.isalpha():
                print("python3 vigenere.py keyword")
                sys.exit(1)
class Cipherguy:
    def doingAlgorithem(self,plaintext,key):

        print("ciphertext: ",end="")

        for index in range(len(plaintext)):

            ciphered = TakingCareOfCiphering(index, plaintext, key)
            return ciphered

        print()

def TakingCareOfCiphering(index, plaintext, key):

    newindex = index % len(key)

    if plaintext[index].isalpha():

        plasse = TakingCareOfCapitalLetter(index, plaintext, key, newindex)
        print(plasse)

        plasse = TakingCareOfCipherSmallLetter(index, plaintext, key, newindex)

    else:

        plasse = plaintext[index]

def TakingCareOfCapitalLetter(index, plaintext, key, newindex):
    if plaintext[index].isupper():

        if key[newindex].isupper():

            asciiletter = (((ord(plaintext[index]) - 65) + (ord(key[newindex]) - 65)) % 26)
            plasse.append(asciiletter)
            return chr(asciiletter + 65)
          #  retun plasse.append(asciiletter)

        elif key[newindex].islower():

            asciiletter = (((ord(plaintext[index]) - 65) + (ord(key[newindex]) - 97)) % 26)

            return chr(asciiletter + 65)
         #   plasse.append(asciiletter)

def TakingCareOfCipherSmallLetter(index, plaintext, key, newindex):

    if plaintext[index].islower():

        if key[newindex].isupper():

            asciiletter = (((ord(plaintext[index]) - 97) + (ord(key[newindex]) - 65)) % 26)

            return chr(asciiletter + 97)
        #    return plasse.append(asciiletter)
        elif key[newindex].islower():

            asciiletter = (((ord(plaintext[index]) - 97) + (ord(key[newindex]) - 97)) % 26)

            return chr(asciiletter + 97)
           # return plasse.append(asciiletter)