"""
Binary Search Tree Implementation 
"""


class TreeNode:
    """ Node for Binary Search Tree class """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        """ In-order iterator """

        # If node is not None
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem

            yield self.key

            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def has_right_child(self):
        """ Returns right child of the node """
        return self.right_child

    def has_left_child(self):
        """ Returns left child of the node """
        return self.left_child

    def has_parent(self):
        """ Returns parent of the node """
        return self.parent

    def is_left_child(self):
        """ Checks if node is a left child """
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        """ Checks if node is a right child """
        return self.parent and self.parent.right_child == self

    def is_root(self):
        """ Checks if node is a root node """
        return not self.parent

    def is_leaf(self):
        """ Checks if node is a leaf node """
        return not (self.left_child and self.right_child)

    def has_child(self):
        """ Checks if node has any child """
        return self.left_child or self.right_child

    def has_children(self):
        """ Checks if node has both children """
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, left_child, right_child):
        """ Replaces node's data """
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

        # Sets left child's parent as the current node
        if self.has_left_child():
            self.left_child.parent = self

        # Sets right child's parent as the current node
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        """ Returns a new successor for the current node """

        succ = None
        # Looks for the smallest child of the right subtree
        if self.has_right_child():
            succ = self.right_child.find_min()

        else:
            # Current node has a parent
            if self.parent:
                # Current node is a left child
                if self.is_left_child():
                    succ = self.parent
                # Current node is a right child
                else:
                    self.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self

        return succ

    def split_out(self):
        """ Changes the references of the current node """

        # Current node is a leaf
        if self.is_leaf():
            # Current node is a left child
            if self.is_left_child():
                self.parent.left_child = None
            # Current node is a right child
            else:
                self.parent.right_child = None

        # Current node has at least one child
        elif self.has_child():
            # Current node has a left child
            if self.has_left_child():
                # Current node is a right child
                if self.is_right_child():
                    self.parent.right_child = self.left_child

                # Current node is a left child
                else:
                    self.parent.left_child = self.left_child

                self.left_child.parent = self.parent

            # Current node has a right child
            else:
                # Current node is a right child
                if self.is_right_child():
                    self.parent.right_child = self.right_child

                # Current node is a left child
                else:
                    self.parent.left_child = self.right_child

                self.right_child.parent = self.parent

    def find_min(self):
        """ Returns the child node with the lowest value """
        current = self
        while current.has_left_child():
            current = current.left_child
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

    def _put(self, key, value, current_node):
        """ Private recursive put call """

        # Replace value if key is the same
        if key == current_node.key:
            current_node.replace_node_data(
                key, value, current_node.left_child, current_node.right_child
            )

        # Place on left sublist
        elif key < current_node.key:
            # Looks recursively until there is no child node left
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)

        # Place on right sublist
        else:
            # Looks recursively until there is no child node left
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def get(self, key):
        """ Gets tree node value from the binary search tree """

        # Check for the value of root node
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, current_node):
        """ Private recursive get call """

        # Node not found
        if not current_node:
            return None

        # Node found
        elif current_node.key == key:
            return current_node

        # Looks recursively on the right subtree
        elif key > current_node.key:
            return self._get(key, current_node.right_child)

        # Looks recursively on the left subtree
        else:
            return self._get(key, current_node.left_child)

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

    def _remove(self, current_node):
        """ Private method to remove the node from the tree """

        # Node has no children
        if current_node.is_leaf():
            # Node to be removed is a left child
            if current_node.parent.left_child == current_node:
                current_node.parent.left_child = None
            # Node to be removed is a right child
            elif current_node.parent.right_child == current_node:
                current_node.parent.right_child = None

        # Node has both left and right children
        elif current_node.has_children():
            succ = current_node.find_successor()
            succ.split_out()
            current_node.key = succ.key
            current_node.value = succ.value

        # Node has just one child
        else:
            # Node to be removed has a left child
            if current_node.has_left_child():
                # Moves current node's left child to parent's left child
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child

                # Moves current node's left child to parent's right child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child

                # Moves current node's left child to the root node
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )

            # Node to be removed has a right child
            elif current_node.has_right_child():
                # Moves current node's right child to parent's left child
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child

                # Moves current node's right child to parent's right child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child

                # Moves current node's right child to the root node
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )


def main():
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
    # num_list = [66, 88, 61, 89, 94, 50, 4, 76, 66, 82]

    # for num in num_list:
    #     tree_test.put(num, num)

    # print("\nPrinting binary search tree with random integers")
    # for num in num_list:
    #     print(tree_test[num])


if __name__ == "__main__":
    main()
