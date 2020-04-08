def move_tower(height, fromPole, toPole, withPole):
    if height >= 1:
        move_tower(height - 1, fromPole, withPole, toPole)
        move_disk(fromPole, toPole)
        move_tower(height - 1, withPole, toPole, fromPole)


def move_disk(fromPole, toPole):
    print("Moving disk from " + str(fromPole) + " to " + str(toPole))


def main():
    move_tower(3, "A", "C", "B")


if __name__ == "__main__":
    main()
