class BinaryTree():
    ''' Binary Tree Node and Reference Implementation '''

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        bt = []

        # Root Node
        if self.key:
            bt.append(self.key)
        else:
            bt.append(None)

        # Left Node
        if self.leftChild:
            bt.append(self.leftChild.key)
        else:
            bt.append(None)

        # Right Node
        if self.rightChild:
            bt.append(self.rightChild.key)
        else:
            bt.append(None)

        return str(bt)

    def insertLeft(self, newNode):
        ''' Adds left node under root node '''

        # No left node available
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        # Left node available
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        ''' Adds right node under root node '''

        # No right node available
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        # Right node available
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        ''' Returns left node '''
        return self.leftChild

    def getRightChild(self):
        ''' Returns right node '''
        return self.rightChild

    def setRootValue(self, obj):
        ''' Sets root value from tree '''
        self.key = obj

    def getRootValue(self):
        ''' Returns root value from tree '''
        return self.key


def buildTree():
    ''' Creates a custom binary tree '''

    # Level One
    root = BinaryTree("a")
    root.insertLeft("b")
    root.insertRight("c")

    # Level Two
    root.getLeftChild().insertRight("d")
    root.getRightChild().insertLeft("e")
    root.getRightChild().insertRight("f")

    print(root)
    print(root.getLeftChild())
    print(root.getRightChild())


def preorder(tree):
    ''' Preorder traversal for binary tree '''
    if tree != None:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    ''' Inorder traversal for binary tree '''

    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootValue())
        inorder(tree.getRightChild())


def postorder(tree):
    ''' Postorder traversal for binary tree '''
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree)


if __name__ == "__main__":
    root = BinaryTree("a")
    print(root.getRootValue())

    # Level One
    root.insertLeft("b")
    print(root.getLeftChild().getRootValue())
    root.insertRight("c")
    print(root.getRightChild().getRootValue())

    # Level Two
    root.getLeftChild().insertLeft("d")
    root.getLeftChild().insertRight("e")
    root.getRightChild().insertLeft("f")
    root.getRightChild().insertRight("g")

    # Programming Language Tree
    language_tree = BinaryTree()
    language_tree.setRootValue("Language")

    # Left Subtree
    language_tree.insertLeft("compiled")
    language_tree.getLeftChild().insertLeft("C")
    language_tree.getLeftChild().insertRight("Java")

    # Right Subtree
    language_tree.insertRight("interpreted")
    language_tree.getRightChild().insertLeft("Python")
    language_tree.getRightChild().insertRight("Scheme")

    
