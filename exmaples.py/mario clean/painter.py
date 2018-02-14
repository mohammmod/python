

class Painter:
    def draw_the_pyramid(self,number):
        for steps in range(number):

            for space in range(number - steps - 1):
                print(" ", end="")
            for hashes in range(steps + 1):
                print("#", end="")
            print("  ", end="")

            for hashess in range(steps + 1):
                print("#", end="")
            print("")