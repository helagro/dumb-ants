import simulation_graphics
from simulation_engine import terrain_generation
from simulation_engine import coord_generation




def generateRandomVacantCoord():
    pass


def init():
    width, height = simulation_graphics.getScreenSize()
    height -= 60

    CORDINATES_X = round(width / 10)
    CORDINATES_Y = round(height / 10)

    simulation_graphics.init(width, height, CORDINATES_X, CORDINATES_Y, coord_generation.DOT_SIZE)
    coord_generation.init(CORDINATES_X, CORDINATES_Y)
    terrain_generation.generateTerrain()