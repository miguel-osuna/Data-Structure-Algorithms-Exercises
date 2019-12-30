# Generates a hash for a given string (Positional Weighting)
def hashForString(str, tablesize):
    sum = 0
    for pos in range(len(str)):
        sum += ord(str[pos]) * (pos + 1)
    return sum % tablesize



if __name__ == "__main__":
    print(hashForString("cat", 11))
    print(hashForString("race", 11))
    print(hashForString("care", 11))
