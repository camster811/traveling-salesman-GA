import random
from TownHelper import TownHelper

class Neighbor:
    def __init__(self, sequence):
        self.sequence = sequence
        self.random = random.Random()

    def get_fitness(self):
        totalDistance = 0.0
        for i in range(len(self.sequence)):
            fromTown = TownHelper.TOWN_POSITIONS[self.sequence[i - 1]]
            toTown = TownHelper.TOWN_POSITIONS[self.sequence[i]]
            
            x = toTown.x - fromTown.x
            y = toTown.y - fromTown.y
            
            d = (x ** 2 + y ** 2) ** 0.5
            totalDistance += d
        
        return totalDistance
    
class World:
    def __init__(self, population_count):
        self.population_count = population_count
        self.neighbors = []

    def spawn(self):
        for _ in range(self.population_count):
            self.neighbors.append(self.generate_neighbor())

    def generate_neighbor(self):
        sequence = [i for i in range(self.population_count)]
        
        randomizer = random.Random()
        sequence = randomizer.sample(sequence, self.population_count)
        
        return Neighbor(sequence)

    def do_generation(self):
        for neighbor in self.neighbors:
            neighbor.get_fitness()
            

    def get_best_neighbor(self):
        return min(self.neighbors, key=lambda n: n.get_fitness(), default=None)
    
    
if __name__ == "__main__":
    world = World(10)
    world.spawn()
    
    for _ in range(10):
        world.do_generation()    
          
    print(world.get_best_neighbor().get_fitness())