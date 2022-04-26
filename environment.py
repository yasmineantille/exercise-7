import tsplib95

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""
class Environment:
    def __init__(self, rho, ant_population):

        self.rho = rho
        self.ant_population = ant_population

        # Initialize the environment topology
        self.topology = tsplib95.load('att48-specs/att48.tsp')
        # Initialize the pheromone map in the environment
        self.pheromone_map = self.initialize_pheromone_map()

    # Task 1.1
    # Initialize the pheromone trails in the environment
    def initialize_pheromone_map(self):
        # L=10628 corresponds to the optimal solution for Pseudo-Euclidean distances among the nodes
        # We could optimize the cost value
        optimal_distance = 10628

        # initial pheromone value = m / C^(nn) where
        # m = nr of ants and C^(nn) expected cost of a tour
        init_value = self.ant_population / (optimal_distance * 2)
        return [[init_value] * self.topology.dimension for _ in range(self.topology.dimension)]

    # Task 1.2
    # Update the pheromone trails in the environment
    def update_pheromone_map(self, ants):
        # step 1: pheromone evaporation
        for i in range(self.topology.dimension):
            for j in range(self.topology.dimension):
                self.pheromone_map[i][j] = (1 - self.rho) * self.pheromone_map[i][j]

        # step 2: Pheromone is then added on the arcs the ants have crossed in their tours
        for ant in ants:
            delta_tau = 1 / ant.travelled_distance
            for loc, loc2 in zip(ant.travelled_locations, ant.travelled_locations[1:]):
                self.pheromone_map[loc-1][loc2-1] = self.pheromone_map[loc-1][loc2-1] + delta_tau

    # Get the pheromone trails in the environment
    def get_pheromone_map(self):
        return self.pheromone_map

    # Get the environment topology
    def get_possible_locations(self):
        return list(self.topology.get_nodes())
