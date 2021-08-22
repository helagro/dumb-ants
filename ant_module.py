from simulation_engine import coord_generation
import simulation_graphics

class Ant:

    def move(self):
        newX, newY = coord_generation.walkRandomDirection(self.x, self.y)
        simulation_graphics.drawAnt(newX, newY, self)
        simulation_graphics.drawBackground(self.x, self.y)
        self.x = newX
        self.y = newY

    def tick(self):
        self.move()

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, colony):
        self.colony = colony
        self.color = colony.color
 
