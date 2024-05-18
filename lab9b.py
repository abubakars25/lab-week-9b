import random

class Agent:
    def __init__(self, identifier, world):
        self.identifier = identifier
        self.world = world
        self.position = None

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.world.size)) for j in range(self.world.size) if self.world.grid[i][j] is None]
        return random.choice(empty_patches) if empty_patches else None

    def move_to_patch(self, patch):
        if self.position:
            self.world.grid[self.position[0]][self.position[1]] = None
        self.position = patch
        self.world.grid[patch[0]][patch[1]] = self.identifier

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(i, self) for i in range(num_agents)]

    def init_world(self):
        for agent in self.agents:
            empty_patch = agent.find_empty_patch()
            if empty_patch:
                agent.move_to_patch(empty_patch)

    def execute(self, iterations):
        for step in range(iterations):
            print(f"Step {step + 1}")
            self.show_grid()
            for agent in self.agents:
                empty_patch = agent.find_empty_patch()
                if empty_patch:
                    agent.move_to_patch(empty_patch)

    def show_grid(self):
        for row in self.grid:
            print(' '.join(['.' if cell is None else str(cell) for cell in row]))
        print()

if __name__ == "__main__":
    world_size = 5
    num_agents = 3
    iterations = 5

    world = World(world_size, num_agents)
    world.init_world()
    world.execute(num_steps)
