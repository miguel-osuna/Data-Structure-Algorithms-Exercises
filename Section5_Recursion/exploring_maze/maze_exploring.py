import turtle
import os

PART_OF_PATH = "o"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


class Maze:
    # Initialices a maze
    def __init__(self, mazeFileName):
        # Setup
        mazeFile = open(mazeFileName, "r")
        self.mazeList = []
        rowsInMaze = 0
        columnsInMaze = 0

        # Read file line by line
        for line in mazeFile:
            col = 0
            rowList = []

            # Read character by character
            for char in line[:-1]:
                rowList.append(char)
                if char == "S":
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1

            rowsInMaze += 1
            self.mazeList.append(rowList)
            columnsInMaze = len(rowList)

        # Sets num of rows and columns as class attributes
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze

        # Sets axis
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2

        # Creates turtle and window object
        self.t = turtle.Turtle(shape="turtle")
        self.w = turtle.Screen()

        # Sets coordinates for bottom left and top right corners respectively
        self.w.setworldcoordinates(
            -(columnsInMaze - 1) / 2 - 0.5,
            -(rowsInMaze - 1) / 2 - 0.5,
            (columnsInMaze - 1) / 2 + 0.5,
            (rowsInMaze - 1) / 2 + 0.5,
        )

    # Operator overloading
    def __getitem__(self, idx):
        return self.mazeList[idx]

    # Draws box
    def drawCenteredBox(self, x, y, color):
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

    # Displays the representation of the Maze
    def drawMaze(self):
        self.t.speed(10)
        self.w.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazeList[y][x] == OBSTACLE:
                    self.drawCenteredBox(
                        x + self.xTranslate, -y + self.yTranslate, "red"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.w.update()
        self.w.tracer(1)

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazeList[row][col] = val
        self.moveTurtle(col, row)

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
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (
            row == 0
            or row == self.rowsInMaze - 1
            or col == 0
            or col == self.columnsInMaze - 1
        )


def searchFrom(maze, startRow, startColumn):
    # Update turtle position
    maze.updatePosition(startRow, startColumn)

    # Try each of four directions from this point until we find a way out
    # Base cases
    # 1. If ran into obstacle, return False
    if maze[startRow][startColumn] == OBSTACLE:
        return False

    # 2. If found a square that has already been explored, return False
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False

    # 3. If found an outside edge not occupied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    #
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logic OR to test other directions
    found = (
        searchFrom(maze, startRow - 1, startColumn)
        or searchFrom(maze, startRow + 1, startColumn)
        or searchFrom(maze, startRow, startColumn - 1)
        or searchFrom(maze, startRow, startColumn + 1)
    )

    if found:
        maze.updatePostion(startRow, startColumn, PART_OF_PATH)

    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)

    return found


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mazeFile = os.path.join(base_dir, "maze_test.txt")

    myMaze = Maze(mazeFile)
    myMaze.drawMaze()
    myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

    searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
