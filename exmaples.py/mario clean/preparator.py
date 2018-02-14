from cs50 import get_int

class Preparator:
    def get_height_in_range(self,minnum,maxnum):
        while True:
            number = get_int("Height: ")
            if number >=minnum and number <=maxnum:
                break

        return number
