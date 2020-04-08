from stack import Stack


def revstring(string):
    stack = Stack()
    rev_string = ""
    for c in string:
        stack.push(c)
    while not stack.is_empty():
        rev_string = rev_string + stack.pop()
    return str(rev_string)


def main():
    print(revstring("Hello"))


if __name__ == "__main__":
    main()
