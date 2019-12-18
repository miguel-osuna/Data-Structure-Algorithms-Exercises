def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    print("Moving disk from " + str(fromPole) + " to " + str(toPole))


if __name__ == "__main__":
    moveTower(3, "A", "C", "B")
