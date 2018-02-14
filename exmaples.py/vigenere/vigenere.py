from helpers import Get,examiner,Cipherguy

key = Get().TheKey(1)
examiner().check_(key)
plainText = Get().ThePlainText("plainText: ")
cipherText = Cipherguy().doingAlgorithem(plainText,key)
print(cipherText)

