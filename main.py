import log
import simulation_engine
import simulation_cycle
import simulation_graphics
from simulation_engine import coord_generation

def main():
    log.log("started")
    simulation_engine.init()
    simulation_cycle.startSim()

main()