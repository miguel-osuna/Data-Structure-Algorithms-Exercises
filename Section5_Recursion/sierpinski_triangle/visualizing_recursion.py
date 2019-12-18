import turtle
import random


def drawSpiral(myTurtle, lineLen, decrement):
    if lineLen > decrement:
        myTurtle.forward(lineLen - decrement)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-decrement, decrement)


def tree(branchLen, t, limit):
    dec = random.randrange(10, 21, 1)

    if branchLen > limit:
        t.width(branchLen / 10)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-dec, t, limit)
        t.left(40)
        tree(branchLen-dec, t, limit)
        t.right(20)
        t.backward(branchLen)


if __name__ == "__main__":
    myTurtle = turtle.Turtle()
    myWindow = turtle.Screen()

    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    myTurtle.color("green")

    # Fractal tree
    tree(75, myTurtle, 5)
    myWindow.exitonclick()
