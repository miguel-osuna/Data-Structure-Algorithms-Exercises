''' 
Binary Tree list of lists implementation.
'''

def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def setRootValue(root, value):
    root[0] = value


def getRootValue(root):
    return root[0]


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def printBinaryTree(root):
    print("\nRoot node: {}".format(root[0]))
    print("Left node: {}".format(root[1]))
    print("Right node: {}".format(root[2]))


def buildTree(a, b, c, d, e, f):
    # Root
    root = BinaryTree(a)
    insertLeft(root, b)
    insertRight(root, c)

    # Left Child
    insertRight(getLeftChild(root), d)

    # Right Child
    insertLeft(getRightChild(root), e)
    insertRight(getRightChild(root), f)

    return root


if __name__ == "__main__":
    r = BinaryTree(0)
    insertLeft(r, "left")
    insertRight(r, "right")

    leftFirstLevel = getLeftChild(r)
    rightFirstLevel = getRightChild(r)

    insertLeft(leftFirstLevel, "left-left-second-level")
    insertRight(leftFirstLevel, "left-right-second-level")

    insertLeft(rightFirstLevel, "right-left-second-level")
    insertRight(rightFirstLevel, "right-right-second-level")

    printBinaryTree(r)

    tree_test = buildTree("a", "b", "c", "d", "e", "f")
    printBinaryTree(tree_test)

    