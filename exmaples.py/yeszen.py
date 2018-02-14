import cs50

n = cs50.get_int("substring")
a = "what the hell bro"
b = "what the fuck bro"
sub_a = [a[x:x+n] for x in range(len(a) - n + 1)]
sub_b = [b[x:x+n] for x in range(len(b) - n + 1)]
print("this is sup a",sub_a)
print("this is sup b",sub_b)

similar = []
for i in sub_a:
    if i in sub_b and i not in similar:
        similar.append(i)

print(similar)
