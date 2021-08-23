import simulation_engine
import time

TICK_DELAY = 0.3
simShouldRun = False

def startSim():
    global simShouldRun
    simShouldRun = True

    while(simShouldRun):
        simulation_engine.tick()
        time.sleep(TICK_DELAY)


def stopSim():
    global simShouldRun
    simShouldRun = False
