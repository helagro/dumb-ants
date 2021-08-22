import log
import simulation_engine
import simulation_cycle

def main():
    log.log(5, "started")
    simulation_engine.init()
    simulation_cycle.startSim()

main()