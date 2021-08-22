import random
import math

CORDINATES_X = None
CORDINATES_Y = None
DOT_SIZE = 1
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
            return newX, newY
        i +=1
        if i > 8: i = 0 

def isCoordVacant():
    pass

def generateRandomCoord():
    x = round(random.uniform(0, CORDINATES_X))
    y = round(random.uniform(0, CORDINATES_Y))
    return x, y

def init(cordinatesX, cordinatesY):
    global CORDINATES_X, CORDINATES_Y
    CORDINATES_X = cordinatesX
    CORDINATES_Y = cordinatesY
