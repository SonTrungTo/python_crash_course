from random import randint

class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides: int = 6):
        """Init a dice instance"""
        self._sides = sides

    def roll_die(self, times: int = 0):
        """Prints a random number between 1 and the number of sides the die has for x times"""
        if (times < 0):
            raise ValueError(f"Invalid times")
        else:
            for _ in range(times):
                print(f"The {self._sides}-sided die shows {randint(1, self._sides)}")

if __name__ == "__main__":
    my_die = Die()
    my_die.roll_die(10)
    ten_th_die = Die(10)
    ten_th_die.roll_die(10)
    twenty_th_die = Die(20)
    twenty_th_die.roll_die(10)
