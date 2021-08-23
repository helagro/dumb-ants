from log import log
import random
import math
import simulation_graphics
import time

CORDINATES_X = None
CORDINATES_Y = None
DOT_SIZE = 1
POSSIBLE_DIRECTIONS = [-DOT_SIZE, 0, DOT_SIZE]
CHANCE_OF_STAYING_ON_COURSE = 4



def getDistance(posX, posY, destX, destY):
    diffX = posX - destX
    diffY = posY - destY
    distance = int(math.sqrt(diffX**2 + diffY**2))
    return distance

def getStraightDirectionToTarget(x, y, targetX, targetY):
    distance = getDistance(x, y, targetX, targetY)
    diffX = targetX - x
    diffY = targetY - y
    direction = {"x":math.ceil(diffX/distance), "y":math.ceil(diffY/distance), "distance":distance}
    return direction

def isCoordVacant(x, y):
    if x > CORDINATES_X or x < 0: pass
    elif y > CORDINATES_Y or y < 0: pass
    elif simulation_graphics.getCoordStatus(x, y) != 0: pass
    else: return True
    return False

def checkArround(outreach, function, xPos, yPos):
    xEdge = xPos - outreach
    yEdge = yPos - outreach
    sideLength = outreach*2+1
    for x in range(xEdge, xEdge + sideLength):
        for y in range(yEdge, yEdge + sideLength):
            if xPos == x and yPos == y:
                continue
            if function(x, y): return

def getDirection(i):
    x = POSSIBLE_DIRECTIONS[(i % 3)]
    y = POSSIBLE_DIRECTIONS[math.floor(i / 3)]
    return x, y

def walkRandomDirection(x, y, lastDirectionI = None):
    i = -1
    if lastDirectionI != None and random.randint(0, 10) <= CHANCE_OF_STAYING_ON_COURSE:
        i = lastDirectionI
    else: i = random.randint(0, 8)

    dirX,dirY = getDirection(i)
    newX = dirX + x
    newY = dirY + y

    if isCoordVacant(newX, newY):
        return newX, newY, i
    return None


def generateRandomVacantCoord():
    while True:
        x = round(random.uniform(0, CORDINATES_X))
        y = round(random.uniform(0, CORDINATES_Y))
        if isCoordVacant(x,y): return x,y

def init(cordinatesX, cordinatesY):
    random.seed(time.time())

    global CORDINATES_X, CORDINATES_Y
    CORDINATES_X = cordinatesX
    CORDINATES_Y = cordinatesY

