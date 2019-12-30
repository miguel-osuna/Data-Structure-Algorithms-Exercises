'''
Binary Search Tree Implementation 
'''


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return str(self.root)

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __next__(self):
        pass

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        self.put(key, item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, item):
        ''' Adds tree node to the binary search tree '''

        if not self.root:
            self.root = TreeNode(key, item)
        else:
            self._put(key, item, self.root)
        self.size += 1

    def _put(self, key, item, currentNode):
        ''' Private recursive put call '''

        # Place on right sublist
        if key > currentNode.key:
            # Looks recursively until there is no child node
            if currentNode.hasRightChild():
                self._put(key, item, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(
                    key, item, parent=currentNode)

        # Place on left sublist
        else:
            # Looks recursively until there is no child node
            if currentNode.hasLeftChild():
                self._put(key, item, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, item, parent=currentNode)

    def get(self, key):
        ''' Gets tree node item from the binary search tree '''
        if self.root:
            return _get(key, self.root)
        else:
            return None

    def _get(self, key, currentNode):
        ''' Private recursive get call '''
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
        # There is more than one node in the tree
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)

            if nodeToRemove != None:
                self.remove(nodeToRemove)
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

    def remove(self, currentNode):
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
            currentNode.item = succ.item

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
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.item,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)

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
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.item,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)


class TreeNode():
    def __init__(self, key, item, left=None, right=None, parent=None):
        self.key = key
        self.item = item
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasRightChild(self):
        return self.leftChild

    def hasLeftChild(self):
        return self.rightChild

    def hasParent(self):
        return self.parent

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild and self.rightChild)

    def hasChild(self):
        return self.leftChild or self.rightChild

    def hasChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, item, leftchild, rightchild):
        self.key = key
        self.item = item
        self.leftchild = leftchild
        self.rightchild = rightchild

        if self.hasLeftChild():
            self.leftchild.parent = self

        if self.hasRightChild():
            self.rightchild.parent = self

    def findSuccessor(self):
        pass

    def findMind(self):
        pass


if __name__ == "__main__":
    pass
