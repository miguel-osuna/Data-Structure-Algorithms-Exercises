import turtle
import random


def draw_spiral(my_turtle, lineLen, decrement):
    if lineLen > decrement:
        my_turtle.forward(lineLen - decrement)
        my_turtle.right(90)
        draw_spiral(my_turtle, lineLen - decrement, decrement)


def tree(branch_len, t, limit):
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
