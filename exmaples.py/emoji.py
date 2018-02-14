import locale
import cs50
import re

def emoji():
    locale.setlocale(locale.LC_ALL, "")
    number = u'\U0001F601'
    letter = [number,U'\U0001F602',U'\U0001F603',U'\U0001F606',U'\U0001F383']
    for i in range(5):
        print(letter[i],end="")
    print("")
    b = cs50.get_string("emoji unicode:")
    number = 0x1f600
    print(number)