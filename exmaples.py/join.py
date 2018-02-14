import cs50
import locale

print("gave some numers")
hand = 0
while 5 >hand:
    number = cs50.get_int("number ")
    array =[number]
    letters = "".join(chr(letter) for letter in array)
    print(letters)
    hand = hand  + 1