from deque import Deque


def is_palindrome(word):
    chardeque = Deque()
    string = "".join(word.split())

    for char in string:
        chardeque.addRear(char)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.removeFront()
        second = chardeque.removeRear()

        if first != second:
            still_equal = False

    return still_equal


if __name__ == "__main__":
    print(is_palindrome("anita lava la tina"))
    print(is_palindrome("lsdkjfskf"))
    print(is_palindrome("radar"))
