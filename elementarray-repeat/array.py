import cs50

place = []
for i in range(5):
    names = cs50.get_string("give me 5 names:")
    place.append(names)
number = cs50.get_int("how many repet:")
index = 0
plaintext = cs50.get_string("plaintext: ")
print("ciphertext: ")
for index in range(len(plaintext)):
        newindex = index % len(place)