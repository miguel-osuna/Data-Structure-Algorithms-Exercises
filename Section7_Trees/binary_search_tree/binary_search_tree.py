"""
Binary Search Tree Implementation 
"""


class TreeNode:
    """ Node for Binary Search Tree """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        """ Inorder iterator """

        # If node is not None
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem

            yield self.key

            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasRightChild(self):
        """ Returns right child of the node """
        return self.rightChild

    def hasLeftChild(self):
        """ Returns left child of the node """
        return self.leftChild

    def hasParent(self):
        """ Returns parent of the node """
        return self.parent

    def isLeftChild(self):
        """ Checks if node is a left child """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """ Checks if node is a right child """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """ Checks if node is a root node """
        return not self.parent

    def isLeaf(self):
        """ Checks if node is a leaf node """
        return not (self.leftChild and self.rightChild)

    def hasChild(self):
        """ Checks if node has any child """
        return self.leftChild or self.rightChild

    def hasChildren(self):
        """ Checks if node has both children """
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, leftchild, rightchild):
        """ Replaces node's data """
        self.key = key
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild

        # Sets left child's parent as the current node
        if self.hasLeftChild():
            self.leftchild.parent = self

        # Sets right child's parent as the current node
        if self.hasRightChild():
            self.rightchild.parent = self

    def findSuccessor(self):
        """ Returns a new successor for the current node """

        succ = None
        # Looks for the smallest child of the right subtree
        if self.hasRightChild():
            succ = self.rightChild.findMin()

        else:
            # Current node has a parent
            if self.parent:
                # Current node is a left child
                if self.isLeftChild():
                    succ = self.parent
                # Current node is a right child
                else:
                    self.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return succ

    def splitOut(self):
        """ Changes the references of the current node """
        # Current node is a leaf
        if self.isLeaf():
            # Current node is a left child
            if self.isLeftChild():
                self.parent.leftChild = None
            # Current node is a right child
            else:
                self.parent.rightChild = None

        # Current node has at least one child
        elif self.hasChild():
            # Current node has a left child
            if self.hasLeftChild():
                # Current node is a right child
                if self.isRightChild():
                    self.parent.rightChild = self.leftChild

                # Current node is a left child
                else:
                    self.parent.leftChild = self.leftChild

                self.leftChild.parent = self.parent

            # Current node has a right child
            else:
                # Current node is a right child
                if self.isRightChild():
                    self.parent.rightChild = self.rightChild

                # Current node is a left child
                else:
                    self.parent.leftChild = self.rightChild

                self.rightChild.parent = self.parent

    def findMin(self):
        """ Returns the child node with the lowest value """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, value):
        if self._get(value, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, value):
        """ Adds tree node to the binary search tree """

        # Check for the value of root node
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, currentNode):
        """ Private recursive put call """

        # Replace value if key is the same
        if key == currentNode.key:
            currentNode.replaceNodeData(
                key, value, currentNode.leftChild, currentNode.rightChild
            )

        # Place on left sublist
        elif key < currentNode.key:
            # Looks recursively until there is no child node left
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)

        # Place on right sublist
        else:
            # Looks recursively until there is no child node left
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def get(self, key):
        """ Gets tree node value from the binary search tree """

        # Check for the value of root node
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, currentNode):
        """ Private recursive get call """

        # Node not found
        if not currentNode:
            return None

        # Node found
        elif currentNode.key == key:
            return currentNode

        # Looks recursively on the right subtree
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)

        # Looks recursively on the left subtree
        else:
            return self._get(key, currentNode.leftChild)

    def delete(self, key):
        """ Deletes a node from the tree """

        # There is more than one node in the tree
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)

            if nodeToRemove != None:
                self._remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")

        # There is just a root node in the tree
        elif self.size == 1 and key == self.root.key == key:
            self.root = None
            self.size -= 1

        # There are no nodes in the tree
        else:
            raise KeyError("Error, key not found in tree")

    def _remove(self, currentNode):
        """ Private method to remove the node from the tree """

        # Node has no children
        if currentNode.isLeaf():
            # Node to be removed is a left child
            if currentNode.parent.leftChild == currentNode:
                currentNode.parent.leftChild = None
            # Node to be removed is a right child
            elif currentNode.parent.rightChild == currentNode:
                currentNode.parent.rightChild = None

        # Node has both left and right children
        elif currentNode.hasChildren():
            succ = currentNode.findSuccessor()
            succ.splitOut()
            currentNode.key = succ.key
            currentNode.value = succ.value

        # Node has just one child
        else:
            # Node to be removed has a left child
            if currentNode.hasLeftChild():
                # Moves current node's left child to parent's left child
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild

                # Moves current node's left child to parent's right child
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild

                # Moves current node's left child to the root node
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.value,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild,
                    )

            # Node to be removed has a right child
            elif currentNode.hasRightChild():
                # Moves current node's right child to parent's left child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild

                # Moves current node's right child to parent's right child
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild

                # Moves current node's right child to the root node
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.value,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild,
                    )


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])

    mytree[6] = "green"
    mytree[2] = "pink"

    print(mytree[6])
    print(mytree[2])

    # del mytree[6]
    # del mytree[2]

    # tree = BinarySearchTree()
    # for i in range(10):
    #     tree[i] = i

    # for i in range(len(tree)):
    #     print(tree[i])

    # for i in reversed(range(10)):
    #     tree[i] = i

    # for i in reversed(range(10)):
    #     print(tree[i])

    # tree_test = BinarySearchTree()
    # numlist = [66, 88, 61, 89, 94, 50, 4, 76, 66, 82]

    # for num in numlist:
    #     tree_test.put(num, num)

    # print("\nPrinting binary search tree with random integers")
    # for num in numlist:
    #     print(tree_test[num])
