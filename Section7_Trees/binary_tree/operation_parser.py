import sys

sys.path.insert(0, "Section4_Basic_Data_Structures/stack")
from stack import Stack
from binary_tree_class import BinaryTree
import operator


def operationParser(operation):
    """ Arithmetic Operation Parser """
    # Variable setup
    string = list(operation)
    operators = "+-/*"
    bool_operators = "&|!^"
    treeStack = Stack()
    tree = BinaryTree("")
    currentTree = tree
    treeStack.push(currentTree)

    # Iterate over the created list
    for char in string:
        if char == "(":
            currentTree.insertLeft("")
            treeStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif char in operators or char in bool_operators:
            currentTree.setRootValue(char)
            currentTree.insertRight("")
            treeStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif char == ")":
            currentTree = treeStack.pop()

        elif char not in (operators or bool_operators or "()"):
            try:
                if char == "F":
                    currentTree.setRootValue(False)
                elif char == "T":
                    currentTree.setRootValue(True)
                else:
                    currentTree.setRootValue(int(char))
                currentTree = treeStack.pop()
            except ValueError:
                raise ValueError("Token {} is not a valid integer".format(char))

    return tree


def evalExpression(tree):
    """ Arithmetic operation evaluator """
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.mul,
    }

    bool_operations = {
        "&": operator.and_,
        "|": operator.or_,
        "^": operator.xor,
        "!": operator.not_,
    }

    left = tree.getLeftChild()
    right = tree.getRightChild()

    if left and right:
        if tree.getRootValue() in operations.keys():
            function = operations[tree.getRootValue()]

        if tree.getRootValue() in bool_operations.keys():
            function = bool_operations[tree.getRootValue()]

        return function(evalExpression(left), evalExpression(right))

    else:
        return tree.getRootValue()


def printExpression(tree):
    """ Arithmetic Operation Printer """
    eval = ""
    operators = "*/+-"
    bool_operators = "&|!^"

    if tree != None:
        rootValue = str(tree.getRootValue())
        leftNode = tree.getLeftChild()
        rightNode = tree.getRightChild()

        if rootValue in operators or rootValue in bool_operators:
            eval += "(" + printExpression(leftNode)
            eval += rootValue
            eval += printExpression(rightNode) + ")"

        else:
            eval += printExpression(leftNode)
            eval += rootValue
            eval += printExpression(rightNode)

    return eval


def main():
    tree = operationParser("((3+4)*5)")
    print(evalExpression(tree))
    print(printExpression(tree))

    tree = operationParser("(((4*8)/6)-3)")
    print(evalExpression(tree))
    print(printExpression(tree))

    boolean_tree = operationParser("(T^F)")
    print(evalExpression(boolean_tree))
    print(printExpression(boolean_tree))


if __name__ == "__main__":
    main()

