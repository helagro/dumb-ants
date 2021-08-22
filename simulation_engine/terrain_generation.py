import random
import simulation_graphics
from simulation_engine import coord_generation
import ant_colony
from simulation_engine import food

STONE_FORMATIONS_AMOUNT = 30
LONGEST_STONE_GROUP = 70
STARTING_COLONIES_AMOUNT = 2

def generateAntNests():
    for i in range(STARTING_COLONIES_AMOUNT):
        x,y = coord_generation.generateRandomVacantCoord()
        colony = ant_colony.AntColony(x, y)
        simulation_graphics.drawAntsNest(x, y, colony)

def walkAStoneFormation(x, y):
    pathLength = round(random.uniform(0, LONGEST_STONE_GROUP))

    for _ in range(pathLength):
        coords = coord_generation.walkRandomDirection(x, y)
        if coords == None:
            break
        x,y = coords
        simulation_graphics.drawStone(x,y)

def generateStones():
    for i in range(STONE_FORMATIONS_AMOUNT):
        x,y = coord_generation.generateRandomVacantCoord()
        simulation_graphics.drawStone(x, y)
        walkAStoneFormation(x,y)

def generateTerrain():
    generateStones()
    generateAntNests()
    food.spawnInitial()