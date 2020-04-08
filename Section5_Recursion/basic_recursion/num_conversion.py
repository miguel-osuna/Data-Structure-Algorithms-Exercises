# Converts a number from decimal base to another using recursion
def to_str(num, base):
    lookup_numbers = "0123456789ABCDEF"

    # Base case
    if num < base:
        return lookup_numbers[num]

    # Recursive case
    else:
        quotient = num // base
        remainder = num % base
        return to_str(quotient, base) + to_str(remainder, base)


# Reverse a string using recursion
def rev_str(string):
    # Base case
    if len(string) == 1:
        return string[0]

    # Recursive case
    else:
        return string[-1:] + rev_str(string[:-1])


# Checks if string is palindrome implementing rev_str()
def isPalindrome(string):
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
    print(isPalindrome("hello"))
    print(rev_str("anita lava la tina"))
    print(isPalindrome("anita lava la tina"))


if __name__ == "__main__":
    main()
