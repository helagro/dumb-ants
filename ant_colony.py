import log
import random

colonies = []
possibleColors = ["cyan4", "red4", "green4", "blue4", "pink4", "yellow4"]

class AntColony:
    def generateColor(self):
        originalI = round(random.uniform(0, len(possibleColors)-1))
        i = originalI

        while True:
            colorIsVacant = True

            for colonie in colonies:
                if possibleColors[i] == colonie.color:
                    colorIsVacant = False

            if colorIsVacant:
                self.color = possibleColors[i]
                return True

            i += 1
            if i == len(possibleColors):
                i == 0

            if i == originalI:
                log.log(1, "ran out of colors!")
                return False


    def __init__(self):
        if not self.generateColor(): return

        colonies.append(self)
