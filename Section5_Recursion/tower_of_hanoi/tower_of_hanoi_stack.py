# Standard library imports
import sys


# Local application imports
sys.path.insert(0, "Section4_Basic_Data_Structures/stack")
from stack import Stack


class TowerOfHanoi:
    """ Tower of Hanoi class """

    def __init__(self, num_disks, src, des, aux):
        self.num_disks = num_disks
        self.src = src
        self.des = des
        self.aux = aux
        self.towers = {src: Stack(), des: Stack(), aux: Stack()}
        for i in range(self.num_disks, 0, -1):
            self.towers[src].push(i)

    def move_disk(self, src, des):
        self.towers[des].push(self.towers[src].pop())
        print("Moving disk from {} to {}".format(str(src), str(des)))

    def move_tower(self, n, src, des, aux):
        if n >= 1:
            self.move_tower(n - 1, src, aux, des)
            self.move_disk(src, des)
            self.move_tower(n - 1, aux, des, src)

    def print_towers(self):
        print("\nSource: {}".format(self.towers[self.src]))
        print("Auxiliary: {}".format(self.towers[self.aux]))
        print("Destination: {}".format(self.towers[self.des]))


def main():
    toh = TowerOfHanoi(3, "A", "C", "B")
    toh.move_tower(3, "A", "C", "B")
    toh.print_towers()


if __name__ == "__main__":
    main()
