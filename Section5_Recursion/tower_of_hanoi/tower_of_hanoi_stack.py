import sys
sys.path.insert(0, "Section4_Basic_Data_Structures/stack")
from stack import Stack


class TowerOfHanoi():
    def __init__(self, numDisks, src, des, aux):
        self.numDisks = numDisks
        self.src = src
        self.des = des
        self.aux = aux
        self.towers = {
            src: Stack(),
            des: Stack(),
            aux: Stack()
        }
        for i in range(self.numDisks, 0, -1):
            self.towers[src].push(i)

    def moveDisk(self, src, des):
        self.towers[des].push(self.towers[src].pop())
        print("Moving disk from {} to {}".format(str(src), str(des)))

    def moveTower(self, n, src, des, aux):
        if n >= 1:
            self.moveTower(n-1, src, aux, des)
            self.moveDisk(src, des)
            self.moveTower(n-1, aux, des, src)

    def printTowers(self):
        print("\nSource: {}".format(self.towers[self.src]))
        print("Auxiliary: {}".format(self.towers[self.aux]))
        print("Destination: {}".format(self.towers[self.des]))


if __name__ == "__main__":
    toh = TowerOfHanoi(3, "A", "C", "B")
    toh.moveTower(3, "A", "C", "B")
    toh.printTowers()
