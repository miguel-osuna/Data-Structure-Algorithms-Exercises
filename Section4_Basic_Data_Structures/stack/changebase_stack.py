# Local application imports
from stack import Stack


def divide_by_base(num, base):
    stack = Stack()
    digits = "0123456789ABCDEF"

    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    binary_num = ""
    while not stack.is_empty():
        binary_num = binary_num + digits[stack.pop()]

    return binary_num


def main():
    print(divide_by_base(233, 2))
    print(divide_by_base(233, 8))
    print(divide_by_base(255, 16))


if __name__ == "__main__":
    main()
