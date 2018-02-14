from cs50 import get_string
import sys
import crypt

possiblty = "abcdefghijklmnopqrstuvwxyzYXCVBNMASDFGHJKLQWERTZUIOP"

class crackPasswprd:
    def check(number):
        if len(sys.argv) != number :
            print("python3 vigenere.py keyword")
            sys.exit(1)
    def oneLetter(TheHash):
        for letter in possiblty:
            cryptoo = crypt.crypt(letter, "50")
            if cryptoo == TheHash:
                print(letter)
                sys.exit(0)
    def twoLetter(Thehash):
        for length in possiblty:
            for length1 in possiblty:
                twoletter = length + length1
                cryptoo = crypt.crypt(twoletter, "50")
                if cryptoo == Thehash:
                    print(twoletter)
                    sys.exit(0)
    def threeLetter(Thehash):
        for letter in possiblty:
            for letter1 in possiblty:
                for letter2 in possiblty:
                    threeletter = letter + letter1 + letter2
                    cryptoo = crypt.crypt(threeletter, "50")
                    if cryptoo == Thehash:
                        print(threeletter)
                        sys.exit(0)

    def fourLetter(Thehash):
        for letter in possiblty:
            for letter1 in possiblty:
                for letter2 in possiblty:
                    for letter3 in possiblty:
                        fourletter = letter + letter1 + letter2 + letter3
                        cryptoo = crypt.crypt(fourletter, "50")
                        if cryptoo == Thehash:
                            print(fourletter)
                            sys.exit(0)
