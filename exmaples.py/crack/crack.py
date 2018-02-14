from crackClasses import crackPasswprd
import sys

def main():
    Thehash = sys.argv[1]
    crackPasswprd.check(2)
    crackPasswprd.oneLetter(Thehash)
    crackPasswprd.twoLetter(Thehash)
    crackPasswprd.threeLetter(Thehash)
    crackPasswprd.fourLetter(Thehash)

if __name__ == "__main__":
    main()