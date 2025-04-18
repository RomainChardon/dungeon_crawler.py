class Enemy: 
    
    def __init__(self, x, y, health = 3, vision_range=5):
        self.x = x
        self.y = y
        self.health = health
        self.vision_range = vision_range

    def hit(self, player):
        self.health -= 1
        
        add_x = self.x - player.x
        add_y = self.y - player.y
        
        # add new location 
        self.x += add_x
        self.y += add_y
        
        return self
        

    def is_player_visible(self, player):
        # TODO : Fontion du périmetre de l'enemie
        pass

    def move_toward_player(self, player, game_map):
        # TODO : Fontion déplacement vers le joueur
        pass

        # TODO : Fonction attaque de l'enemi