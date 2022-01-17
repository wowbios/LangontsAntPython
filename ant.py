import enum
from pygame.locals import Color

class Direction(enum.Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

class AntRL:
    def __init__(self, w, h, x, y, color):
        self.color = color
        self.width = w
        self.height = h
        self.pos = (x, y)
        self.dir = Direction.Up
        self.moves = {
            Direction.Up: self.__moveUp,
            Direction.Right: self.__moveRight,
            Direction.Down: self.__moveDown,
            Direction.Left: self.__moveLeft,
        }
        self.rights = {
            Direction.Up: Direction.Right,
            Direction.Right: Direction.Down,
            Direction.Down: Direction.Left,
            Direction.Left: Direction.Up,
        }
        self.lefts = {
            Direction.Up: Direction.Left,
            Direction.Right: Direction.Up,
            Direction.Down: Direction.Right,
            Direction.Left: Direction.Down,
        }

    def act(self, state):
        if state == 0:
            self.__turnRight()
            self.__move()
            return 1
        elif state == 1:
            self.__turnLeft()
            self.__move()
            return 0
        else:
            raise "WRONG"

    def __move(self):
        self.moves[self.dir]()

    def __turnRight(self):
        self.dir = self.rights[self.dir]

    def __turnLeft(self):
        self.dir = self.lefts[self.dir]

    def __moveUp(self):
        self.pos = ((self.pos[0] + self.height - 1) % self.height, self.pos[1])

    def __moveDown(self):
        self.pos = ((self.pos[0] + 1) % self.height, self.pos[1])

    def __moveLeft(self):
        self.pos = (self.pos[0], (self.pos[1] + self.width - 1) % self.width)

    def __moveRight(self):
        self.pos = (self.pos[0], (self.pos[1] + 1) % self.width)

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Matrix = [[0 for x in range(width)] for y in range(height)]

    def print(self):
        for i in range(self.height):
            print(' '.join(map(str, self.Matrix[i])))

    def tick(self, ants):
        events = []
        for ant in ants:
            prevPos = ant.pos
            prevState = self.Matrix[prevPos[0]][prevPos[1]]
            newState = ant.act(prevState)
            self.Matrix[prevPos[0]][prevPos[1]] = newState
            events.append((prevPos, self.__getColor(newState, ant.color)))
            events.append((ant.pos, Color(255, 0, 0)))

        return events

    def __getColor(self, state, antColor):
        if state == 0:
            return Color(0,0,0)
        elif state == 1:
            return antColor
        else:
            return Color(100, 0, 0)
