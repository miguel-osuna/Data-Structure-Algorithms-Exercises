def to_str(num, base):
    """ Converts a number from a decimal base to another base using recurssion"""
    lookup_numbers = "0123456789ABCDEF"

    # Base case
    if num < base:
        return lookup_numbers[num]

    # Recursive case
    else:
        quotient = num // base
        remainder = num % base
        return to_str(quotient, base) + to_str(remainder, base)


def rev_str(string):
    """ Reverse a string using recursion """
    # Base case
    if len(string) == 1:
        return string[0]

    # Recursive case
    else:
        return string[-1:] + rev_str(string[:-1])


def is_palindrome(string):
    """ Checks if string is palindrome implementing rev_str()"""
    str = "".join(string.split())
    revstr = rev_str(str)

    if str == revstr:
        return True

    else:
        return False


def main():
    print(to_str(769, 10))
    print(to_str(769, 2))
    print(to_str(769, 16))

    print(rev_str("hello"))
    print(is_palindrome("hello"))
    print(rev_str("anita lava la tina"))
    print(is_palindrome("anita lava la tina"))


if __name__ == "__main__":
    main()
