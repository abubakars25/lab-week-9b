import random

class Entity:
    def __init__(self, identifier, environment):
        self.identifier = identifier
        self.environment = environment
        self.location = None

    def locate_empty_spot(self):
        empty_spots = [(x, y) for x in range(self.environment.dimension) for y in range(self.environment.dimension) if self.environment.matrix[x][y] is None]
        return random.choice(empty_spots) if empty_spots else None

    def shift_to_spot(self, spot):
        if self.location:
            self.environment.matrix[self.location[0]][self.location[1]] = None
        self.location = spot
        self.environment.matrix[spot[0]][spot[1]] = self.identifier

class Environment:
    def __init__(self, dimension, total_entities):
        self.dimension = dimension
        self.matrix = [[None for _ in range(dimension)] for _ in range(dimension)]
        self.entities = [Entity(i, self) for i in range(total_entities)]

    def setup(self):
        for entity in self.entities:
            spot = entity.locate_empty_spot()
            if spot:
                entity.shift_to_spot(spot)

    def execute_simulation(self, iterations):
        for iteration in range(iterations):
            print(f"Iteration {iteration + 1}")
            self.show_environment()
            for entity in self.entities:
                spot = entity.locate_empty_spot()
                if spot:
                    entity.shift_to_spot(spot)

    def show_environment(self):
        for row in self.matrix:
            print(' '.join(['.' if cell is None else str(cell) for cell in row]))
        print()

if __name__ == "__main__":
    environment_size = 5
    total_entities = 3
    total_iterations = 5

    ecosystem = Environment(environment_size, total_entities)
    ecosystem.setup()
    ecosystem.execute_simulation(total_steps)
