def hash_for_string(str, tablesize):
    """ Generates a hash for a given string (Positional Weighting)"""
    sum = 0
    for pos in range(len(str)):
        sum += ord(str[pos]) * (pos + 1)
    return sum % tablesize


def main():
    print(hash_for_string("cat", 11))
    print(hash_for_string("race", 11))
    print(hash_for_string("care", 11))


if __name__ == "__main__":
    main()
