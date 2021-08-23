import log
import simulation_engine
import simulation_cycle
import simulation_graphics
from simulation_engine import coord_generation

def main():
    log.log(5, "started")
    simulation_engine.init()
    right = 0
    left = 0
    simulation_graphics.drawDot(50, 50, "black")
    for i in range(10000000):
        x, y = coord_generation.walkRandomDirection(50, 50)
        if x == 51: right += 1
        if x == 49: left += 1
    print("exp", left, right)
    simulation_cycle.startSim()

main()