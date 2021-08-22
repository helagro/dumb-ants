import simulation_graphics
import random
import sys
import math

CORDINATES_X = None
CORDINATES_Y = None
DOT_SIZE = 1
STONE_FORMATIONS_AMOUNT = 30
LONGEST_STONE_GROUP = 30
POSSIBLE_DIRECTIONS = [-DOT_SIZE, 0, DOT_SIZE]


def isValidCoord(x, y):
    if x > CORDINATES_X or x < 0: pass
    elif y > CORDINATES_Y or y < 0: pass
    else: return True
    return False


def getDirection(i):
    x = POSSIBLE_DIRECTIONS[i % 3]
    y = POSSIBLE_DIRECTIONS[math.floor(i / 3)]
    return x, y

def walkRandomDirection(x, y):
    i = round(random.uniform(0, 8))

    while True:
        dirX,dirY = getDirection(i)
        newX = dirX + x
        newY = dirY + y
        if isValidCoord(newX, newY):
            print(newX, newY)
            return newX, newY
        i +=1
        if i > 8: i = 0 

def walkAStoneFormation(x, y):
    pathLength = round(random.uniform(0, LONGEST_STONE_GROUP))

    for _ in range(pathLength):
        x,y = walkRandomDirection(x, y)
        simulation_graphics.drawStone(x,y)

def generateRandomCoord():
    print("dwa", CORDINATES_X)
    sys.stdout.flush()
    x = round(random.uniform(0, CORDINATES_X))
    y = round(random.uniform(0, CORDINATES_Y))
    return x, y

def generateStones():
    for i in range(STONE_FORMATIONS_AMOUNT):
        x,y = generateRandomCoord()
        simulation_graphics.drawStone(x, y)
        walkAStoneFormation(x,y)


        

def generateTerrain():
    generateStones()

def init():
    global CORDINATES_X
    global CORDINATES_Y
    width, height = simulation_graphics.getScreenSize()
    height -= 60

    CORDINATES_X = round(width / 10)
    CORDINATES_Y = round(height / 10)

    simulation_graphics.init(width, height, CORDINATES_X, CORDINATES_Y, DOT_SIZE)
    generateTerrain()