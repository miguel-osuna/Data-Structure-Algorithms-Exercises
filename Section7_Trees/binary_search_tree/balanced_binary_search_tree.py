from binary_search_tree import TreeNode, BinarySearchTree


class BalancedTreeNode(TreeNode):
    def __init__(self, key, value, left=None, right=None, parent=None, balanceFactor=0):
        super().__init__(key, value, left, right, parent)
        self.balanceFactor = balanceFactor


class BalancedBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        ''' Adds balanced tree node to the balanced binary search tree '''

        # Check for the value of root node
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BalancedTreeNode(key, value)
        self.size += 1

    def _put(self, key, value, currentNode):
        ''' Overrides BinarySearchTree class method '''
        # Place on left sublist
        if key < currentNode.key:
            # Looks recursively until there is no left child node left
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = BalancedTreeNode(
                    key, value, parent=currentNode)
                self.updateBalance(currentNode.leftChild)

        # Place on right sublist
        else:
            # Looks recursively until there is no right child node left
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = BalancedTreeNode(
                    key, value, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, currentNode):
        ''' Recursive call to update node's balance factor '''
        if currentNode.balanceFactor > 1 or currentNode.balanceFactor < -1:
            self.rebalance(currentNode)
            return

        # Current node is not the tree's root
        if currentNode.parent != None:

            # Increment current node parent balance factor by one
            if currentNode.isLeftChild():
                currentNode.parent.balanceFactor += 1
            # Decrement current node parent balance factor by one
            elif currentNode.isRightChild():
                currentNode.parent.balanceFactor -= 1

        # Balance factor of parent has not been adjusted to zero
        if currentNode.parent.balanceFactor != 0:
            self.updateBalance(currentNode.parent)

    def rebalance(self, node):
        # Checks left subtree status for tree rotation
        if node.balanceFactor < 0:
            # Balancing right child and root node
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            # Balancing root node directly
            else:
                self.rotateLeft(node)
        # Checks right subtree status for tree rotation
        elif node.balanceFactor > 0:
            # Balancing left child and root node
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(root.leftChild)
                self.rotateRight(node)
            # Balancing root node directly
            else:
                self.rotateRight(node)

    def rotateLeft(oldRoot):
        # Store the new root node
        newRoot = oldRoot.rightChild

        # Assign new root's left child to old root's right child
        oldRoot.rightChild = newRoot.leftChild

        # Change left child's parent to old root
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = oldRoot

        # Assign old root's parent to new root's parent
        newRoot.parent = oldRoot.parent

        # Parent's node is a root node
        if oldRoot.isRoot():
            self.root = newRoot
        # Parent's left node is the old root
        elif oldRoot.isLeftChild():
            oldRoot.parent.leftChild = newRoot
        # Parent's right node is the old root
        else:
            oldRoot.parent.rightChild = newRoot

        # Change old root's parent to new root node
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot

        # Update balance factor of old and new root nodes
        oldRoot.balanceFactor += 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor += 1 + max(oldRoot.balanceFactor, 0)

    def rotateRight(oldRoot):
        # Store the new root node
        newRoot = oldRoot.leftChild

        # Assign new root's right child to old root's left child
        oldRoot.leftChild = newRoot.rightChild

        # Change right child's node parent to old root
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = oldRoot

        # Assign old root's parent to new root's parent
        newRoot.parent = oldRoot.parent

        # Parent's node is a root node
        if oldRoot.isRoot():
            self.root = newRoot
        # Parent's left node is the old root
        elif oldRoot.isLeftChild():
            oldRoot.parent.leftChild = newRoot
        # Parent's right node is the old root
        else:
            oldRoot.parent.rightChild = newRoot

        # Change old root's parent to new root node
        oldRoot.parent = newRoot
        newRoot.rightChild = oldRoot

        # Update balance factor of old and new root nodes
        oldRoot.balanceFactor -= 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor -= 1 + max(0, oldRoot.balanceFactor)


if __name__ == "__main__":
    node = BalancedTreeNode(0, "A", 0)
    tree = BalancedBinarySearchTree()
    print("Tree created")
