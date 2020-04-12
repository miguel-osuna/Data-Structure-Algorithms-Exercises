class BinaryTree:
    """ Binary Tree Node and Reference Implementation class"""

    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None

    def __str__(self):
        bt = []

        # Root Node
        if self.key:
            bt.append(self.key)
        else:
            bt.append(None)

        # Left Node
        if self.left_child:
            bt.append(self.left_child.key)
        else:
            bt.append(None)

        # Right Node
        if self.right_child:
            bt.append(self.right_child.key)
        else:
            bt.append(None)

        return str(bt)

    def insert_left(self, newNode):
        """ Adds left node under root node """

        # No left node available
        if self.left_child == None:
            self.left_child = BinaryTree(newNode)
        # Left node available
        else:
            t = BinaryTree(newNode)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, newNode):
        """ Adds right node under root node """

        # No right node available
        if self.right_child == None:
            self.right_child = BinaryTree(newNode)
        # Right node available
        else:
            t = BinaryTree(newNode)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        """ Returns left node """
        return self.left_child

    def get_right_child(self):
        """ Returns right node """
        return self.right_child

    def set_root_value(self, obj):
        """ Sets root value from tree """
        self.key = obj

    def get_root_value(self):
        """ Returns root value from tree """
        return self.key


def build_tree():
    """ Creates a custom binary tree """

    # Level One
    root = BinaryTree("a")
    root.insert_left("b")
    root.insert_right("c")

    # Level Two
    root.get_left_child().insert_right("d")
    root.get_right_child().insert_left("e")
    root.get_right_child().insert_right("f")

    print(root)
    print(root.get_left_child())
    print(root.get_right_child())


def preorder(tree):
    """ Preorder traversal for binary tree """
    if tree != None:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree):
    """ Inorder traversal for binary tree """

    if tree != None:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())


def postorder(tree):
    """ Postorder traversal for binary tree """
    if tree != None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree)


def main():
    root = BinaryTree("a")
    print(root.get_root_value())

    # Level One
    root.insert_left("b")
    print(root.get_left_child().get_root_value())
    root.insert_right("c")
    print(root.get_right_child().get_root_value())

    # Level Two
    root.get_left_child().insert_left("d")
    root.get_left_child().insert_right("e")
    root.get_right_child().insert_left("f")
    root.get_right_child().insert_right("g")

    # Programming Language Tree
    language_tree = BinaryTree("c")
    language_tree.set_root_value("Language")

    # Left Subtree
    language_tree.insert_left("compiled")
    language_tree.get_left_child().insert_left("C")
    language_tree.get_left_child().insert_right("Java")

    # Right Subtree
    language_tree.insert_right("interpreted")
    language_tree.get_right_child().insert_left("Python")
    language_tree.get_right_child().insert_right("Scheme")


if __name__ == "__main__":
    main()
