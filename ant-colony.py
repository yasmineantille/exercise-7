import random
import numpy as np

from environment import Environment
from ant import Ant

# Class representing the ant colony
"""
    ant_population: the number of ants in the ant colony
    iterations: the number of iterations 
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
    rho: pheromone evaporation rate
"""


class AntColony:
    def __init__(self, ant_population: int, iterations: int, alpha: float, beta: float, rho: float):
        self.ant_population = ant_population
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        # Initialize the environment of the ant colony
        self.environment = Environment(self.rho, self.ant_population)

        # Initilize the list of ants of the ant colony
        self.ants = []

        # get random init location
        random_init_location = self.get_random_location()

        # Initialize the ants of the ant colony
        for i in range(ant_population):
            # Initialize an ant on a random initial location
            ant = Ant(self.alpha, self.beta, random_init_location)

            # Position the ant in the environment of the ant colony so that it can move around
            ant.join(self.environment)

            # Add the ant to the ant colony
            self.ants.append(ant)

    # returns a random possible location
    def get_random_location(self):
        return random.choice(self.environment.get_possible_locations())

    # resets the ant colony environment to the init status
    def reset(self):
        self.ants = []
        random_init_location = random.choice(self.environment.get_possible_locations())
        for i in range(self.ant_population):
            ant = Ant(self.alpha, self.beta, random_init_location)
            ant.join(self.environment)
            self.ants.append(ant)

    # Task 1.5
    # Solve the ant colony optimization problem  
    def solve(self):

        # The solution will be a list of the visited cities
        solution = []

        # Initially, the shortest distance is set to infinite
        shortest_distance = np.inf
        for i in range(self.iterations):
            print(f"Running iteration: {i + 1}")

            for ant in self.ants:
                ant.run()
                if ant.travelled_distance < shortest_distance:
                    shortest_distance = ant.travelled_distance
                    solution = ant.travelled_locations

                # update environment
                self.environment.update_pheromone_map(self.ants)
                # Reset ant
                ant.reset(self.get_random_location())

            # Reset ant colony environment for next iteration
            self.reset()

        return solution, shortest_distance


def main():
    # Intialize the ant colony
    ant_colony = AntColony(50, 10, 0, 5, 0.5)

    # Solve the ant colony optimization problem
    solution, distance = ant_colony.solve()
    print("Solution: ", solution)
    print("Distance: ", distance)


if __name__ == '__main__':
    main()
