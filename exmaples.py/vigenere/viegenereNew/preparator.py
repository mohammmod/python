import sys

class Perparator:
    def check_length(self):
        if len(sys.argv) != 2:
            print("python3 vigenere.py keyword")
            return sys.exit(1)

    def check_isalpha(self,word):
        for letter in word:
            if not letter.isalpha():
                print("python3 vigenere.py keyword")
                sys.exit(1)