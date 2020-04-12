# Standard library imports
import random

# Third party imports
import turtle


def draw_spiral(my_turtle, line_len, decrement):
    """ Draw a spiral """
    if line_len > decrement:
        my_turtle.forward(line_len - decrement)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - decrement, decrement)


def tree(branch_len, t, limit):
    """ Draw a tree """
    dec = random.randrange(10, 21, 1)

    if branch_len > limit:
        t.width(branch_len / 10)
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - dec, t, limit)
        t.left(40)
        tree(branch_len - dec, t, limit)
        t.right(20)
        t.backward(branch_len)


def main():
    my_turtle = turtle.Turtle()
    myWindow = turtle.Screen()

    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")

    # Fractal tree
    tree(75, my_turtle, 5)
    myWindow.exit_on_click()


if __name__ == "__main__":
    main()
