import random
import simulation_graphics
from simulation_engine import coord_generation
import ant_colony

STONE_FORMATIONS_AMOUNT = 30
LONGEST_STONE_GROUP = 30
STARTING_COLONIES_AMOUNT = 2

def walkAStoneFormation(x, y):
    pathLength = round(random.uniform(0, LONGEST_STONE_GROUP))

    for _ in range(pathLength):
        x,y = coord_generation.walkRandomDirection(x, y)
        simulation_graphics.drawStone(x,y)

def generateStones():
    for i in range(STONE_FORMATIONS_AMOUNT):
        x,y = coord_generation.generateRandomCoord()
        simulation_graphics.drawStone(x, y)
        walkAStoneFormation(x,y)


def generateAntNests():
    for i in range(STARTING_COLONIES_AMOUNT):
        colony = ant_colony.AntColony()
        x,y = coord_generation.generateRandomCoord()
        simulation_graphics.drawAntsNest(x, y, colony)

def generateTerrain():
    generateStones()
    generateAntNests()