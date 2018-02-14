import cs50

def main():
    number = cs50.get_int("number: ")
    something = "what about us what about the life"
    somethin2 = "how can i live how can breath what"
    liste = []
    liste2 = []
    # قاك قاك
    for i in range(len(somethin2) - number + 1 ):
        liste.append(somethin2[i:i+number])
    liste = list(liste)
    # kak
    for j in range(len(something)- number + 1):
        liste2.append(something[j:j+number])
    liste2 = list(liste2)
    print("this is list",liste)
    print("this is just another one", liste2)
    liseo = []
    # kak
    for c in liste:
        if c in liste2 and liste not in liseo:
            liseo.append(c)
    print("the similer substring",liseo)
if __name__ == "__main__":
    main()
# array []
# array.append(a[[begin:begin + h])
# return array