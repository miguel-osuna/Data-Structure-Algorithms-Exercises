""" Fraction data type class """


def gcd(m, n):
    """ This
    is a test"""
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        if type(top) != type(1):
            raise Exception("The numerator should be an integer")

        elif type(bottom) != type(1):
            raise Exception("The denominator should be an integer")

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        """ Addition """
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """ Subtraction """
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """ Multiplication """
        new_num = self.num * other.num
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """ Division """
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        """ Equality """
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __ne__(self, other):
        """ Not Equal """
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num

    def __lt__(self, other):
        """ Less than """
        if self.num / self.den < other.num / other.den:
            return True
        else:
            return False

    def __le__(self, other):
        """ Less equal """
        if self.num / self.den <= other.num / other.den:
            return True
        else:
            return False

    def __gt__(self, other):
        """ Greater than """
        if self.num / self.den > other.num / other.den:
            return True
        else:
            return False

    def __ge__(self, other):
        """ Greater equal """
        if self.num / self.den >= other.num / other.den:
            return True
        else:
            return False

    def show(self):
        print(self.num, "/", self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


def main():
    x = Fraction(-1, 0)
    y = Fraction(2, 3)
    print(x)
    print(y)
    print(x + y)
    print(x == y)
    print(x * y)
    print(x > y)
    print(x < y)
    print(x - y)
    print(x.get_num())
    print(x.get_den())


if __name__ == "__main__":
    main()
