import cs50


SoSo = cs50.get_string()
##place = [len(SoSo) - 1]
i = 0
for i in range(len(SoSo)):
    if SoSo.isalpha():
        print(SoSo[i])
    else:
        place = SoSo[i]

print(place)