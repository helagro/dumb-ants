import random
import simulation_graphics
from simulation_engine import coord_generation
import ant_colony
from simulation_engine import food
import log

STONE_FORMATIONS_AMOUNT = 30
LONGEST_STONE_GROUP = 150
STARTING_COLONIES_AMOUNT = 2

def generateAntNests():
    for i in range(STARTING_COLONIES_AMOUNT):
        x,y = coord_generation.generateRandomVacantCoord()
        colony = ant_colony.AntColony(x, y)
        simulation_graphics.drawAntsNest(x, y, colony)

def walkAStoneFormation(x, y):
    pathLength = round(random.uniform(0, LONGEST_STONE_GROUP))
    directionI = None

    for _ in range(pathLength):
        coords = coord_generation.walkRandomDirection(x, y, directionI)
        if coords == None:
            break
        x, y, directionI = coords
        simulation_graphics.drawStone(x,y)

def generateStones():
    print("l0")
    for i in range(STONE_FORMATIONS_AMOUNT):
        log.log(i, "0")
        x,y = coord_generation.generateRandomVacantCoord()
        log.log(i, "1")
        simulation_graphics.drawStone(x, y)
        log.log(i, "2")
        walkAStoneFormation(x,y)
        log.log(i, "3")
    print("l1")

def generateTerrain():
    log.log("dwa")
    generateStones()
    log.log("fesfes")
    generateAntNests()
    food.spawnInitial()
    log.log("Generated Terrain")