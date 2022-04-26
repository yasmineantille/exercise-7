# Class representing an artificial ant of the ant colony
"""
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
"""
import random


class Ant():
    def __init__(self, alpha: float, beta: float, initial_location):
        self.alpha = alpha
        self.beta = beta
        self.current_location = initial_location
        self.travelled_distance = 0
        self.travelled_locations = []
        self.possible_locations = set()

    def reset(self, initial_location):
        self.current_location = initial_location
        self.travelled_distance = 0
        self.travelled_locations = []
        self.possible_locations = set()

    # Task 1.4
    # The ant runs to visit all the possible locations of the environment 
    def run(self):
        self.travelled_locations.append(self.current_location)  # Add initial loc to travelled list
        pos_locations = self.environment.get_possible_locations()
        self.possible_locations = [loc for loc in pos_locations if loc not in self.travelled_locations]

        while len(self.possible_locations) > 0:
            next_location = self.select_path()
            print(f"next loc: {next_location}")
            distance = self.get_distance(self.current_location, next_location)
            print(f"distance: {distance}")
            self.travelled_distance += distance
            print(f"total distance: {self.travelled_distance}")
            #print(f"travelled distance: {self.travelled_distance}")
            self.current_location = next_location
            self.possible_locations.remove(self.current_location) # remove "next" loc from possible list
            self.travelled_locations.append(self.current_location) # add "next" loc to travelled list

    # Task 1.3
    # Select the next path based on the random proportional rule of the ACO algorithm
    def select_path(self):
        probabilities = {}
        total = 0
        for loc in list(self.possible_locations):
            # pheromone map starts at 0 so subtract 1 to identifiers
            amount_of_pheromone = self.environment.pheromone_map[self.current_location-1][loc-1]
            heuristic_value = 1.0 / self.get_distance(self.current_location, loc)
            probability = amount_of_pheromone ** self.alpha * heuristic_value ** self.beta
            probabilities[loc] = probability
            total += probability

        if total > 0:
            for prob in probabilities.keys():
                probabilities[prob] = probabilities[prob] / total

        # the following random choice gives really bad distances (total distances in the end > 50'000)
        #next_location = random.choice(list(probabilities))
        # therefore went with random choices instead
        next_location = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
        return next_location

    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment

    # Task 1.3
    # Get the distance between two nodes
    def get_distance(self, node_a, node_b):
        edge = node_a, node_b
        return self.environment.topology.get_weight(*edge)
