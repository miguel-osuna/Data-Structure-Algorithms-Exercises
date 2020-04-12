def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print("Moving disk from " + str(from_pole) + " to " + str(to_pole))


def main():
    move_tower(3, "A", "C", "B")


if __name__ == "__main__":
    main()
