import random


class MSDie:
    """
    Multi-sided die

    Properties:
        current_value
        num_sides

    Methods:
        roll()
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}): {}".format(self.num_sides, self.current_value)

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides + 1)
        return self.current_value


if __name__ == "__main__":
    die = MSDie(6)
    print(die)
