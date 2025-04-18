class game_map:
    def __init__(self, width, height, wall_chance=0.1):
        self.width = width
        self.height = height
        self.wall_chance = wall_chance # wall spawn rate
        self.grid = self.generate_game_map()

    def generate_game_map(self):
        import random
        grid = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                
                # border of dungeon
                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    row.append('#')  # add a border wall
                else:
                    if random.random() < self.wall_chance:
                        row.append('#')
                    # wall spread, add wall_chance / 2 chance if there is a neighbor
                    elif y > 1 and x > 1:
                        if (grid[y - 2][x - 1] == '#' or grid[y - 1][x - 2] == '#') and random.random() < self.wall_chance * 0.5:
                            row.append('#') # add wall 
                        else:
                            row.append(' ') # add ground
                    else:
                        row.append(' ')  # add ground
            grid.append(row)

        return grid


    def is_walkable(self, x, y):
        # return True if is a ground
        return self.grid[y][x] == ' '
    
    def is_escape(self, x, y):
        # return True if is a escape
        return self.grid[y][x] == 'S'


    def display(self, player, enemies):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"PV : {player.health} / x : {player.x} / y : {player.y}")
        for e in enemies:
            print(f"Ennemi : {e.health} / x : {e.x} / y : {e.y}")

        for y in range(self.height):
            line = ''
            for x in range(self.width):
                if player.x == x and player.y == y:
                    line += '@'  # player
                elif any(e.x == x and e.y == y for e in enemies):
                    line += 'E'  # enemi
                else:
                    line += self.grid[y][x]
            print(line)
            
        



