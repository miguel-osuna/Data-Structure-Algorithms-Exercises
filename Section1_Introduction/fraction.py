''' Fraction data type class '''


def gcd(m, n):
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
        ''' Addition '''
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        ''' Subtraction '''
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        ''' Multiplication '''
        newnum = self.num * other.num
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        ''' Division '''
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        ''' Equality '''
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        ''' Not Equal '''
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum

    def __lt__(self, other):
        ''' Less than '''
        if self.num / self.den < other.num / other.den:
            return True
        else:
            return False

    def __le__(self, other):
        ''' Less equal '''
        if self.num / self.den <= other.num / other.den:
            return True
        else:
            return False

    def __gt__(self, other):
        ''' Greater than '''
        if self.num / self.den > other.num / other.den:
            return True
        else:
            return False

    def __ge__(self, other):
        ''' Greater equal '''
        if self.num / self.den >= other.num / other.den:
            return True
        else:
            return False

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


if __name__ == "__main__":
    x = Fraction(-1, 0)
    y = Fraction(2, 3)
    print(x)
    print(y)
    print(x+y)
    print(x == y)
    print(x * y)
    print(x > y)
    print(x < y)
    print(x-y)
    print(x.getNum())
    print(x.getDen())
