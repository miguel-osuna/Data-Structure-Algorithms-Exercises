# Standard library imports
import os

# Third party imports 
import turtle

PART_OF_PATH = "o"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


class Maze:
    """ Maze class """

    def __init__(self, maze_file_name):
        """ Initialices a maze"""
        # Setup
        maze_file = open(maze_file_name, "r")
        self.maze_list = []
        rows_in_maze = 0
        columns_in_maze = 0

        # Read file line by line
        for line in maze_file:
            col = 0
            row_list = []

            # Read character by character
            for char in line[:-1]:
                row_list.append(char)
                if char == "S":
                    self.start_row = rows_in_maze
                    self.start_col = col
                col += 1

            rows_in_maze += 1
            self.maze_list.append(row_list)
            columns_in_maze = len(row_list)

        # Sets num of rows and columns as class attributes
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze

        # Sets axis
        self.x_translate = -columns_in_maze / 2
        self.y_translate = rows_in_maze / 2

        # Creates turtle and window object
        self.t = turtle.Turtle(shape="turtle")
        self.w = turtle.Screen()

        # Sets coordinates for bottom left and top right corners respectively
        self.w.set_world_coordinates(
            -(columns_in_maze - 1) / 2 - 0.5,
            -(rows_in_maze - 1) / 2 - 0.5,
            (columns_in_maze - 1) / 2 + 0.5,
            (rows_in_maze - 1) / 2 + 0.5,
        )

    def __getitem__(self, idx):
        """ Operator overloading """
        return self.maze_list[idx]

    def draw_centered_box(self, x, y, color):
        """" Draws box """
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def draw_maze(self):
        """ Displays the representation of the Maze """
        self.t.speed(10)
        self.w.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -y + self.y_translate, "red"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.w.update()
        self.w.tracer(1)

    def move_turtle(self, x, y):
        """ Move turtle in the box """
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        """ Drop a bread crumb """
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        """ Update position of the turtle """
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "yellow"
        else:
            color = None

        if color:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        """ Check if turtle exits """
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )


def search_from(maze, start_row, start_column):
    """ Search turtle position """

    maze.update_position(start_row, start_column)

    # Try each of four directions from this point until we find a way out
    # Base cases
    # 1. If ran into obstacle, return False
    if maze[start_row][start_column] == OBSTACLE:
        return False

    # 2. If found a square that has already been explored, return False
    if (
        maze[start_row][start_column] == TRIED
        or maze[start_row][start_column] == DEAD_END
    ):
        return False

    # 3. If found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    #
    maze.update_position(start_row, start_column, TRIED)

    # Otherwise, use logic OR to test other directions
    found = (
        search_from(maze, start_row - 1, start_column)
        or search_from(maze, start_row + 1, start_column)
        or search_from(maze, start_row, start_column - 1)
        or search_from(maze, start_row, start_column + 1)
    )

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)

    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    maze_file = os.path.join(base_dir, "maze_test.txt")

    myMaze = Maze(maze_file)
    myMaze.draw_maze()
    myMaze.update_position(myMaze.start_row, myMaze.start_col)

    search_from(myMaze, myMaze.start_row, myMaze.start_col)


if __name__ == "__main__":
    main()
