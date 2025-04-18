from .Map import game_map
from .Player import Player
from .Enemy import Enemy
import time
import os
import sys

class Game:
    def __init__(self):
        self.game_map = game_map(20, 10)
        self.player = Player(1, 1)
        self.enemies = [Enemy(10, 5)]
        self.running = True

    def handle_input(self):  
        try:
            import termios
            import tty
            def getch():
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch
        except ImportError:
            import msvcrt
            def getch():
                return msvcrt.getch().decode()
                
        key = getch().lower()

        # TODO : Ajout touche pour coup d'epee
        if key == 'z':
            self.player.move(self.game_map, 0, -1)
        elif key == 's':
            self.player.move(self.game_map, 0, 1)
        elif key == 'q':
            self.player.move(self.game_map, -1, 0)
        elif key == 'd':
            self.player.move(self.game_map, 1, 0)
        elif key == ' ':
            self.player.attack(self.game_map, self.enemies)            
        elif key == 'x':
            self.running = False
            
        self.game_map.display(self.player, self.enemies)
            

    def update_enemies(self):
        for enemy in self.enemies:
            if enemy.is_player_visible(self.player):
                enemy.move_towards_player(self.player, self.game_map)

    def run(self):
        while self.running:
            self.game_map.display(self.player, self.enemies)
            self.handle_input()
            self.update_enemies()
            time.sleep(0.1)