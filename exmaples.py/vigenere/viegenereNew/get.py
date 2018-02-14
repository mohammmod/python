from cs50 import get_string
import sys

class new_scanner:
    def get_key(self):
        return sys.argv[1]

    def get_plaintext(self,message):
        return get_string(message)
