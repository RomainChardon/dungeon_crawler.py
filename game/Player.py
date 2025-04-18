class Player: 
    def __init__(self, x, y, health=3, stop_game=False):
        self.x = x
        self.y = y
        self.health = health

    def move(player, game_map, dx, dy): 
        new_x = player.x + dx
        new_y = player.y + dy
        
        if game_map.is_walkable(new_x, new_y):       
            player.x, player.y, = new_x, new_y
            return player
        elif game_map.is_escape(new_x, new_y):
            player.x, player.y, = new_x, new_y
            return player
        
    def attack(player, game_map, enemies): 
        import time
        
        slash_location = [
            [player.x, player.y-1], # top
            [player.x, player.y+1], # bottom
            [player.x-1 , player.y], # left
            [player.x+1 , player.y] # right
        ]

        save_grid={}
        
        for x, y in slash_location:
            save_grid[(x, y)] = game_map.grid[y][x] # save old element in grid 
            print(game_map.grid[y][x])                    
            if game_map.grid[y][x] == ' ':
                game_map.grid[y][x] = '+'
            else: 
                for e in enemies:
                    if e.x == x and e.y == y :
                        print(e)
                        e.hit(player)
                        game_map.grid[y][x] = 'x'
                    # TODO enenemi touche, chercher dans la listes des enemies le quel est touché et lui enlever de la vie. Quand il est touché il recule d'une case
                
        # show slash
        game_map.display(player, enemies)
        time.sleep(0.2)

        # reset element in grid
        for (x, y), old_value in save_grid.items():
            game_map.grid[y][x] = old_value
            
        return enemies
                                

    # TODO : Function d'attaque
    # TODO : Function de perte de point de vie
            
            
            
        