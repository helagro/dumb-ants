import simulation_engine

simShouldRun = False

def startSim():
    global simShouldRun
    simShouldRun = True

    simulation_engin.init()
    while(simShouldRun):
        pass


def stopSim():
    global simShouldRun
    simShouldRun = False
