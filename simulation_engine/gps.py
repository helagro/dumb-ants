from log import log
from simulation_engine import coord_generation

class Gps():

    def guessIsBigger(self, coordIndex, i):
        opponent = self.regiteredLocations[i]

        return coordIndex > opponent


    def binarySearch(self, coordIndex):
        smallestAbove = len(self.regiteredLocations) -1
        biggestUnderneath = 0
        while True:
            guessI = round((smallestAbove - biggestUnderneath) / 2 + biggestUnderneath)
            guessIsBiggerAns = self.guessIsBigger(coordIndex,guessI)

            if guessIsBiggerAns: biggestUnderneath = guessI
            else: smallestAbove: smallestAbove = guessI
            if(smallestAbove - biggestUnderneath <= 1): return smallestAbove


    def findRightPosition(self, coordIndex, i):
        if len(self.regiteredLocations) == 0 or self.guessIsBigger(coordIndex, len(self.regiteredLocations)-1): return -1
        return self.binarySearch(coordIndex)


    def locationIsStoredOrRegister(self, x, y):
        coordIndex = x * 100000 + y
        i = self.findRightPosition(coordIndex, round(len(self.regiteredLocations) / 2))

        if(i != -1 and coordIndex == self.regiteredLocations[i]):
            #print("Already has specie")
            return True

        if(i == -1): self.regiteredLocations.append(coordIndex)
        else: self.regiteredLocations.insert(i, coordIndex)

        return False


    def getRoute(self, x, y, targetX, targetY):
        self.points = [{"x":x, "y":y, "directionsTo": [{"x":0, "y":0}]}]

        while True:
            for i in range(len(self.points)):
                log(2, "trust me" + str(i))
                point = self.points[i]
                for directionI in range(8):
                    x, y = coord_generation.getDirection(directionI)

                    newX = point["x"]+x
                    newY = point["y"]+y

                    if newX == targetX and newY == targetY: return point["directionsTo"] + [{"x":x, "y":y}]
                    if not coord_generation.isCoordVacant(newX, newY): continue
                    if self.locationIsStoredOrRegister(newX, newY): continue

                    self.points.insert(0, {"x":newX, "y":newY, "directionsTo":point["directionsTo"]+[{"x":x, "y":y}]})
                    i += 1
                    log(2, "trust me pal" + str(i) + str(self.points))
                    del self.points[i]
            print("i am")
            



    def __init__(self):
        self.points = []
        self.regiteredLocations = []