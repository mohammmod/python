import time
import datetime
now = datetime.datetime.now()
print(now.year,now.month , now.day)

year = time.strftime("%Y")
print( year)
yeare = int(input("number: "))

if yeare < int(now.year) :
    print("rejected")
else:
    print("accepted")
