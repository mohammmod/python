from algorithms import vigenere_cipher

class Cipher:
    def cipher(self,plaintext,key):
        print("ciphertext: ",end="")
        ciphertext = []
        counter = 0
        for index in range(len(plaintext)):

            if plaintext[index].isalpha():

                keyindex = counter % len(key)

                if plaintext[index].islower():
                    vlaue = 97
                    if key[keyindex].islower():
                        asciiletter = 97

                        cipherletter = vigenere_cipher().cipher_lowercase_letter(plaintext,key,index,keyindex,vlaue,asciiletter)

                        ciphertext.append(cipherletter)

                    if key[keyindex].isupper():
                        asciiletter = 65

                        cipherletter = vigenere_cipher().cipher_uppercase_letter(plaintext,key,index,keyindex,vlaue,asciiletter)

                        ciphertext.append(cipherletter)

                if plaintext[index].isupper():
                    vlaue = 65

                    if key[keyindex].islower():

                        asciiletter = 97

                        cipherletter = vigenere_cipher().cipher_lowercase_letter(plaintext,key,index,keyindex,vlaue,asciiletter)

                        ciphertext.append(cipherletter)

                    if key[keyindex].isupper():

                        asciiletter = 65

                        cipherletter = vigenere_cipher().cipher_uppercase_letter(plaintext,key,index,keyindex,vlaue,asciiletter)

                        ciphertext.append(cipherletter)

                counter +=1

            else:
                ciphertext.append(plaintext[index])

        return ''.join(ciphertext)

