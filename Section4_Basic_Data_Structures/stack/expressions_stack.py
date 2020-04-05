from stack import Stack


def infixToPostfix(expression):
    """ Converts expression from infix to postfix """

    # Operator precedence object
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    # Lists
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    postfix_list = []
    token_list = expression.split()

    # Stack
    opstack = Stack()

    # Check for tokens
    for token in token_list:
        if token in letters or token in numbers:
            postfix_list.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top_token = opstack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = opstack.pop()

        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())

    return " ".join(postfix_list)


def postfixEval(expression):
    # Stack
    operandstack = Stack()

    # List
    token_list = expression.split()

    # String
    numbers = "0123456789"

    # Nested function for operations
    def do_math(num1, num2, operation):
        if operation == "/":
            return num1 / num2

        elif operation == "*":
            return num1 * num2

        elif operation == "+":
            return num1 + num2

        elif operation == "-":
            return num1 - num2

    for token in token_list:
        if token in numbers:
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = do_math(operand1, operand2, token)
            operandstack.push(result)

    return operandstack.pop()


def main():
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    print(postfixEval("4 5 6 * +"))
    print(postfixEval("7 8 + 3 2 + /"))
    print(postfixEval("1 1 + 3 * 9 /"))


if __name__ == "__main__":
    main()
