from simulation_engine import coord_generation
import simulation_engine
import simulation_graphics
import math
from simulation_engine import food
from simulation_engine import gps

class Ant:

    def die(self):
        self.colony.hunterGatherers.remove(self)
        simulation_graphics.drawBackground(self.x, self.y)

    def eatFood(self, x, y):
        food.foodAmount -= 1
        simulation_graphics.drawBackground(x, y)
        #self.hasFood = True

    def move(self):
        newX = None
        newY = None

        if len(self.directions) != 0:
            print(self.directions)
            newX = self.x + self.directions[0]["x"]
            newY = self.y + self.directions[0]["y"]
            del self.directions[0]
            if not coord_generation.isCoordVacant(newX, newY): return
        else:
            newPos = coord_generation.walkRandomDirection(self.x, self.y, self.lastDirectionI)
            if newPos == None: return
            newX, newY, lastDirectionI = newPos
            self.lastDirectionI = lastDirectionI

        if self.x == newX and self.y == newY: return

        simulation_graphics.drawAnt(newX, newY, self)
        simulation_graphics.drawBackground(self.x, self.y)
        self.x = newX
        self.y = newY

    def lookAtPlace(self, x, y):
        thingAtPlace = simulation_graphics.getCoordStatus(x, y)
        if thingAtPlace == 0: return False
        distanceFromAnt = math.floor(coord_generation.getDistance(self.x, self.y, x, y))

        if isinstance(thingAtPlace, Ant) and thingAtPlace.colony != self.colony:
            self.directions = gps.Gps().getRoute(self.x, self.y, x, y)
            if distanceFromAnt == 1:
                thingAtPlace.die()
        elif thingAtPlace == "food" and not self.hasFood:
            if distanceFromAnt == 1:
                self.eatFood(x, y)
            else:

                self.directions = gps.Gps().getRoute(self.x, self.y, x, y)

        #print("look", thingAtPlace, self.color, distanceFromAnt)

    def lookAround(self):
        coord_generation.checkArround(4, self.lookAtPlace, self.x, self.y)

    def tick(self):
        self.lookAround()
        self.move()

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, colony):
        self.colony = colony
        self.color = colony.color
        self.lastDirectionI = None
        self.hasFood = False
        self.directions = []
 
