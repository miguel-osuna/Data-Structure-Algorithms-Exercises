from binary_search_tree import TreeNode, BinarySearchTree


class BalancedTreeNode(TreeNode):
    def __init__(
        self, key, value, left=None, right=None, parent=None, balance_factor=0
    ):
        super().__init__(key, value, left, right, parent)
        self.balance_factor = balance_factor


class BalancedBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        """ Adds balanced tree node to the balanced binary search tree """

        # Check for the value of root node
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BalancedTreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        """ Overrides BinarySearchTree class method """
        # Place on left sublist
        if key < current_node.key:
            # Looks recursively until there is no left child node left
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = BalancedTreeNode(
                    key, value, parent=current_node
                )
                self.update_balance(current_node.left_child)

        # Place on right sublist
        else:
            # Looks recursively until there is no right child node left
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = BalancedTreeNode(
                    key, value, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, current_node):
        """ Recursive call to update node's balance factor """
        if current_node.balance_factor > 1 or current_node.balance_factor < -1:
            self.rebalance(current_node)
            return

        # Current node is not the tree's root
        if current_node.parent != None:

            # Increment current node parent balance factor by one
            if current_node.is_left_child():
                current_node.parent.balance_factor += 1
            # Decrement current node parent balance factor by one
            elif current_node.is_right_child():
                current_node.parent.balance_factor -= 1

        # Balance factor of parent has not been adjusted to zero
        if current_node.parent.balance_factor != 0:
            self.update_balance(current_node.parent)

    def rebalance(self, node):
        # Checks left subtree status for tree rotation
        if node.balance_factor < 0:
            # Balancing right child and root node
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            # Balancing root node directly
            else:
                self.rotate_left(node)
        # Checks right subtree status for tree rotation
        elif node.balance_factor > 0:
            # Balancing left child and root node
            if node.left_child.balance_factor < 0:
                self.rotate_left(root.left_child)
                self.rotate_right(node)
            # Balancing root node directly
            else:
                self.rotate_right(node)

    def rotate_left(old_root):
        # Store the new root node
        new_root = old_root.right_child

        # Assign new root's left child to old root's right child
        old_root.right_child = new_root.left_child

        # Change left child's parent to old root
        if new_root.left_child != None:
            new_root.left_child.parent = old_root

        # Assign old root's parent to new root's parent
        new_root.parent = old_root.parent

        # Parent's node is a root node
        if old_root.is_root():
            self.root = new_root
        # Parent's left node is the old root
        elif old_root.is_left_child():
            old_root.parent.left_child = new_root
        # Parent's right node is the old root
        else:
            old_root.parent.right_child = new_root

        # Change old root's parent to new root node
        old_root.parent = new_root
        new_root.left_child = old_root

        # Update balance factor of old and new root nodes
        old_root.balance_factor += 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor += 1 + max(old_root.balance_factor, 0)

    def rotate_right(old_root):
        # Store the new root node
        new_root = old_root.left_child

        # Assign new root's right child to old root's left child
        old_root.left_child = new_root.right_child

        # Change right child's node parent to old root
        if new_root.right_child != None:
            new_root.right_child.parent = old_root

        # Assign old root's parent to new root's parent
        new_root.parent = old_root.parent

        # Parent's node is a root node
        if old_root.is_root():
            self.root = new_root
        # Parent's left node is the old root
        elif old_root.is_left_child():
            old_root.parent.left_child = new_root
        # Parent's right node is the old root
        else:
            old_root.parent.right_child = new_root

        # Change old root's parent to new root node
        old_root.parent = new_root
        new_root.right_child = old_root

        # Update balance factor of old and new root nodes
        old_root.balance_factor -= 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor -= 1 + max(0, old_root.balance_factor)


def main():
    node = BalancedTreeNode(0, "A", 0)
    tree = BalancedBinarySearchTree()
    print("Tree created")


if __name__ == "__main__":
    main()
