# Standard library imports
import sys
import operator

# Local application imports
sys.path.insert(0, "Section4_Basic_Data_Structures/stack")
from stack import Stack
from binary_tree_class import BinaryTree


def operation_parser(operation):
    """ Arithmetic Operation Parser """
    # Variable setup
    string = list(operation)
    operators = "+-/*"
    bool_operators = "&|!^"
    tree_stack = Stack()
    tree = BinaryTree("")
    current_tree = tree
    tree_stack.push(current_tree)

    # Iterate over the created list
    for char in string:
        if char == "(":
            current_tree.insert_left("")
            tree_stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif char in operators or char in bool_operators:
            current_tree.set_root_value(char)
            current_tree.insert_right("")
            tree_stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif char == ")":
            current_tree = tree_stack.pop()

        elif char not in (operators or bool_operators or "()"):
            try:
                if char == "F":
                    current_tree.set_root_value(False)
                elif char == "T":
                    current_tree.set_root_value(True)
                else:
                    current_tree.set_root_value(int(char))
                current_tree = tree_stack.pop()
            except ValueError:
                raise ValueError("Token {} is not a valid integer".format(char))

    return tree


def eval_expression(tree):
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

    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        if tree.get_root_value() in operations.keys():
            function = operations[tree.get_root_value()]

        if tree.get_root_value() in bool_operations.keys():
            function = bool_operations[tree.get_root_value()]

        return function(eval_expression(left), eval_expression(right))

    else:
        return tree.get_root_value()


def print_expression(tree):
    """ Arithmetic Operation Printer """
    eval = ""
    operators = "*/+-"
    bool_operators = "&|!^"

    if tree != None:
        root_value = str(tree.get_root_value())
        left_node = tree.get_left_child()
        right_node = tree.get_right_child()

        if root_value in operators or root_value in bool_operators:
            eval += "(" + print_expression(left_node)
            eval += root_value
            eval += print_expression(right_node) + ")"

        else:
            eval += print_expression(left_node)
            eval += root_value
            eval += print_expression(right_node)

    return eval


def main():
    tree = operation_parser("((3+4)*5)")
    print(eval_expression(tree))
    print(print_expression(tree))

    tree = operation_parser("(((4*8)/6)-3)")
    print(eval_expression(tree))
    print(print_expression(tree))

    boolean_tree = operation_parser("(T^F)")
    print(eval_expression(boolean_tree))
    print(print_expression(boolean_tree))


if __name__ == "__main__":
    main()
