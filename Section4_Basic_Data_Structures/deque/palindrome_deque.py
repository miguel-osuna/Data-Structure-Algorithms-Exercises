from deque import Deque


def is_palindrome(word):
    chardeque = Deque()
    string = "".join(word.split())

    for char in string:
        chardeque.add_rear(char)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.remove_front()
        second = chardeque.remove_rear()

        if first != second:
            still_equal = False

    return still_equal


def main():
    print(is_palindrome("anita lava la tina"))
    print(is_palindrome("lsdkjfskf"))
    print(is_palindrome("radar"))


if __name__ == "__main__":
    main()
