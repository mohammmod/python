import cs50

name = cs50.get_string()
number = 0;
for letter in name:
    number = number + 1
    print(number,end="")

print("")