import random
import simulation_graphics
from simulation_engine import terrain_generation
from simulation_engine import coord_generation
from simulation_engine import food
import ant_colony


def tick():
    for colony in ant_colony.colonies: 
        colony.balanceInhabitants()
    food.spawnFood()



def init():
    width, height = simulation_graphics.getScreenSize()
    height -= 60
    CORDINATES_X = round(width / 10)
    CORDINATES_Y = round(height / 10)
    simulation_graphics.init(width, height, CORDINATES_X, CORDINATES_Y, coord_generation.DOT_SIZE)
    coord_generation.init(CORDINATES_X, CORDINATES_Y)

    terrain_generation.generateTerrain()