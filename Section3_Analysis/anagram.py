def is_anagram(s1, s2):
    """ Anagram solution with O(n) or O(n log n)"""
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


def anagramSolution2(s1, s2):
    """ Sort and Compare anagram solution with O(n) or O(n log n)"""
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(list1) and matches:
        if list1[pos] == list2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagramSolution3(s1, s2):
    """ Brute Force anagram solution is O(n!) (not a good solution) """
    pass


def anagramSolution4(s1, s2):
    """ Count and Compare anagram solution is O(n), but requires more space"""

    # List of counters
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    match = True
    while j < 26 and match:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            match = False

    return match


def main():
    print(is_anagram("jabon", "banjo"))
    print(anagramSolution2("jabon", "banjo"))
    print(anagramSolution4("jabon", "banjo"))


if __name__ == "__main__":
    main()
