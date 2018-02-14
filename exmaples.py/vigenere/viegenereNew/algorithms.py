
class vigenere_cipher:

    def cipher_lowercase_letter(self,plaintext,key,index,keyindex,vlaue,asciiletter):
        cipertext = ((ord(plaintext[index]) - vlaue) + (ord(key[keyindex]) - asciiletter)) %26
        cipertext = cipertext +vlaue
        return chr(cipertext)
    def cipher_uppercase_letter(self,plaintext,key,index,keyindex,vlaue,asciiletter):
        cipertext = ((ord(plaintext[index]) - vlaue) + (ord(key[keyindex]) - asciiletter)) %26
        cipertext += vlaue
        return chr(cipertext)