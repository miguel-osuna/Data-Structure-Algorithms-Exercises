"""
Binary Tree list of lists implementation.
"""


def BinaryTree(r):
    """ Returns a binary tree as a list """
    return [r, [], []]


def insert_left(root, new_branch):
    """ Adds left node under root node as a list """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    """ Adds right node under root node as a list """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def set_root_value(root, value):
    """ Changes the root value of the tree """
    root[0] = value


def get_root_value(root):
    """ Returns the root value of the tree """
    return root[0]


def get_left_child(root):
    """ Returns the left child of the root as a list """
    return root[1]


def get_right_child(root):
    """ Returns the right child of the root as a list """
    return root[2]


def print_binary_tree(root):
    """ Prints root, left and right node of the binary tree """
    print("\nRoot node: {}".format(root[0]))
    print("Left node: {}".format(root[1]))
    print("Right node: {}".format(root[2]))


def build_tree(a, b, c, d, e, f):
    """ Creates a custom binary tree """
    # Root
    root = BinaryTree(a)
    insert_left(root, b)
    insert_right(root, c)

    # Left Child
    insert_right(get_left_child(root), d)

    # Right Child
    insert_left(get_right_child(root), e)
    insert_right(get_right_child(root), f)

    return root


def main():
    r = BinaryTree(0)
    insert_left(r, "left")
    insert_right(r, "right")

    left_first_level = get_left_child(r)
    right_first_level = get_right_child(r)

    insert_left(left_first_level, "left-left-second-level")
    insert_right(left_first_level, "left-right-second-level")

    insert_left(right_first_level, "right-left-second-level")
    insert_right(right_first_level, "right-right-second-level")

    print_binary_tree(r)

    tree_test = build_tree("a", "b", "c", "d", "e", "f")
    print_binary_tree(tree_test)

    r = BinaryTree(3)
    insert_left(r, 4)
    print(r)

    insert_left(r, 5)
    print(r)

    insert_right(r, 6)
    print(r)

    insert_right(r, 7)
    print(r)

    set_root_value(r, 9)
    insert_left(r, 11)
    print(r)


if __name__ == "__main__":
    main()
