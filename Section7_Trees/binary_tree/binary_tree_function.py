'''
Binary Tree list of lists implementation.
'''


def BinaryTree(r):
    ''' Returns a binary tree as a list '''
    return [r, [], []]


def insertLeft(root, newBranch):
    ''' Adds left node under root node as a list '''
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    ''' Adds right node under root node as a list '''
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def setRootValue(root, value):
    ''' Changes the root value of the tree '''
    root[0] = value


def getRootValue(root):
    ''' Returns the root value of the tree '''
    return root[0]


def getLeftChild(root):
    ''' Returns the left child of the root as a list '''
    return root[1]


def getRightChild(root):
    ''' Returns the right child of the root as a list '''
    return root[2]


def printBinaryTree(root):
    ''' Prints root, left and right node of the binary tree '''
    print("\nRoot node: {}".format(root[0]))
    print("Left node: {}".format(root[1]))
    print("Right node: {}".format(root[2]))


def buildTree(a, b, c, d, e, f):
    ''' Creates a custom binary tree '''
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

    r = BinaryTree(3)
    insertLeft(r, 4)
    print(r)

    insertLeft(r, 5)
    print(r)

    insertRight(r, 6)
    print(r)

    insertRight(r, 7)
    print(r)

    setRootValue(r, 9)
    insertLeft(r, 11)
    print(r)
