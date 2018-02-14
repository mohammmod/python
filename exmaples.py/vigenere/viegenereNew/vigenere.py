from get import new_scanner
from preparator import Perparator
from cipher import Cipher

scanner = new_scanner()
cipher_guy = Cipher()

Perparator().check_length()
key = scanner.get_key()
Perparator().check_isalpha(key)
plaintext = scanner.get_plaintext("plaintext: ")
cipher_Text = cipher_guy.cipher(plaintext,key)
print(cipher_Text)

