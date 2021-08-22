import random
import simulation_graphics
from simulation_engine import coord_generation

INITIAL_FOOD_AMOUNT = 30
FOOD_SPAWN_CHANCE_PER_TICK = 0.1
FOOD_LIMIT = 40
foodAmount = 0

def spawnInitial():
    for _ in range(INITIAL_FOOD_AMOUNT): spawnFood(True)

def spawnFood(forceSpawn = False):
    global foodAmount
    if random.uniform(0, 1) > FOOD_SPAWN_CHANCE_PER_TICK and not forceSpawn: return
    elif foodAmount >= FOOD_LIMIT: return

    x,y = coord_generation.generateRandomVacantCoord()
    simulation_graphics.drawFood(x, y)
    foodAmount += 1