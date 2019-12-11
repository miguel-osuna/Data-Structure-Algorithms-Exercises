from stack import Stack


def divideByBase(num, base):
    stack = Stack()
    digits = "0123456789ABCDEF"

    while num > 0:
        rem = num % base
        stack.push(rem)
        num = num // base

    binary_num = ""
    while not stack.isEmpty():
        binary_num = binary_num + digits[stack.pop()]

    return binary_num


if __name__ == "__main__":
    print(divideByBase(233, 2))
    print(divideByBase(233, 8))
    print(divideByBase(255, 16))
