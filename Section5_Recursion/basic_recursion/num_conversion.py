# Converts a number from decimal base to another using recursion
def toStr(num, base):
    lookup_numbers = "0123456789ABCDEF"

    # Base case
    if num < base:
        return lookup_numbers[num]

    # Recursive case
    else:
        quotient = num // base
        remainder = num % base
        return toStr(quotient, base) + toStr(remainder, base)


# Reverse a string using recursion
def revStr(string):
    # Base case
    if len(string) == 1:
        return string[0]

    # Recursive case
    else:
        return string[-1:] + revStr(string[:-1])


# Checks if string is palindrome implementing revStr()
def isPalindrome(string):
    str = "".join(string.split())
    revstr = revStr(str)

    if str == revstr:
        return True

    else:
        return False


def main():
    print(toStr(769, 10))
    print(toStr(769, 2))
    print(toStr(769, 16))

    print(revStr("hello"))
    print(isPalindrome("hello"))
    print(revStr("anita lava la tina"))
    print(isPalindrome("anita lava la tina"))


if __name__ == "__main__":
    main()
