def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    print("{}! = {}".format(5, factorial(5)))


if __name__ == "__main__":
    main()
