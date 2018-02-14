
something = "how\nare\nyou\nbro\nwahhs\n\n"
something2  ="\nbro\nyou\nare\nwhat\ndude\nare\nyou\nwahhs\nhow"

for line in something,something2:
    place = something.split('\n')
    place2 = something2.split('\n')
bro =[]
for i in place:
    if i in place2 and i:
        print(i)