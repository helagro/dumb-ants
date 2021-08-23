import log
import random
from simulation_engine import food
from simulation_engine import coord_generation
import ant_module
import simulation_graphics

INITIAL_INHABITANTS = 2
POSSIBLE_COLORS = ["cyan", "green", "blue", "pink", "yellow"]
colonies = []

class AntColony:
    def eatFood():
        food.foodAmount -= 1

    def leaveNest(self, x, y):
        if not coord_generation.isCoordVacant(x, y): return False
        ant = self.inhabitants[0]
        ant.setPos(x, y)
        del self.inhabitants[0]
        self.hunterGatherers.append(ant)
        simulation_graphics.drawAnt(x, y, ant)
        return True


    def balanceInhabitants(self):
        amountInhabitants = len(self.inhabitants)
        amountHunterGatherers = len(self.hunterGatherers)

        rightAmountOfHunterGatherers = round(amountInhabitants + amountHunterGatherers * 0.66)
        difference = rightAmountOfHunterGatherers - amountHunterGatherers
        
        for _ in range(difference):
            coord_generation.checkArround(1, self.leaveNest, self.x, self.y)

    def tick(self):
        for ant in self.hunterGatherers:
            ant.tick()
        self.balanceInhabitants()

    def getNestColor(self):
        return self.color + "4"

    def generateColor(self):
        originalI = round(random.uniform(0, len(POSSIBLE_COLORS)-1))
        i = originalI

        while True:
            colorIsVacant = True

            for colonie in colonies:
                if POSSIBLE_COLORS[i] == colonie.color:
                    colorIsVacant = False

            if colorIsVacant:
                self.color = POSSIBLE_COLORS[i]
                return True

            i += 1
            if i == len(POSSIBLE_COLORS):
                i = 0

            if i == originalI:
                log.log(1, "ran out of colors!")
                return False

    def __init__(self, x, y):
        self.x = x
        self.y = y

        if not self.generateColor(): return

        self.inhabitants = []
        self.hunterGatherers = []
        for _ in range(INITIAL_INHABITANTS):
            ant = ant_module.Ant(self)
            self.inhabitants.append(ant)

        colonies.append(self)
