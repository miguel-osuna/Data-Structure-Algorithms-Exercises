import sys
sys.path.insert(0, "Section4_Basic_Data_Structures/stack")
from stack import Stack
import operator
from binary_tree_class import BinaryTree


def operationParser(operation):
    ''' Arithmetic Operation Parser '''
    # Variable setup
    string = list(operation)
    operators = "+-/*"
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

        elif char in operators:
            currentTree.setRootValue(char)
            currentTree.insertRight("")
            treeStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif char == ")":
            currentTree = treeStack.pop()

        elif char not in (operators or "()"):
            try:
                currentTree.setRootValue(int(char))
                currentTree = treeStack.pop()
            except ValueError:
                raise ValueError(
                    "Token {} is not a valid integer".format(char))

    return tree


def evalExpression(tree):
    ''' Arithmetic operation evaluator '''
    operations = {"+": operator.add, "-": operator.sub,
                  "*": operator.mul, "/": operator.mul}

    left = tree.getLeftChild()
    right = tree.getRightChild()

    if left and right:
        function = operations[tree.getRootValue()]
        return function(evalExpression(left), evalExpression(right))

    else:
        return tree.getRootValue()


def printExpression(tree):
    ''' Arithmetic Operation Printer '''
    eval = ""
    if tree != None:
        eval += "(" + printExpression(tree.getLeftChild())
        eval += str(tree.getRootValue())
        eval += printExpression(tree.getRightChild()) + ")"
    return eval


if __name__ == "__main__":
    tree = operationParser("((3+4)*5)")
    print(evalExpression(tree))
    print(printExpression(tree))

    tree = operationParser("(((4*8)/6)-3)")
    print(evalExpression(tree))
    print(printExpression(tree))
