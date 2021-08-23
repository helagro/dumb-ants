from simulation_engine import coord_generation
import simulation_engine
import simulation_graphics
import math
from simulation_engine import food

class Ant:

    def eatFood(self, x, y):
        food.foodAmount -= 1
        simulation_graphics.drawBackground(x, y)
        #self.hasFood = True

    def move(self):
        newPos = coord_generation.walkRandomDirection(self.x, self.y, self.directionI)
        if newPos == None: return

        newX, newY, directionI = newPos
        simulation_graphics.drawAnt(newX, newY, self)
        simulation_graphics.drawBackground(self.x, self.y)
        self.x = newX
        self.y = newY
        self.directionI = directionI

    def lookAtPlace(self, x, y):
        thingAtPlace = simulation_graphics.getCoordStatus(x, y)
        if thingAtPlace == 0: return False
        distanceFromAnt = math.floor(coord_generation.getDistance(self.x, self.y, x, y))

        if thingAtPlace == "food" and distanceFromAnt == 1 and not self.hasFood:
            self.eatFood(x, y)

        #print("look", thingAtPlace, self.color, distanceFromAnt)

    def lookAround(self):
        coord_generation.checkArround(2, self.lookAtPlace, self.x, self.y)

    def tick(self):
        self.lookAround()
        self.move()

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, colony):
        self.colony = colony
        self.color = colony.color
        self.directionI = None
        self.hasFood = False
 
