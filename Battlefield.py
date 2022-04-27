# import Fleet and Herd
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.welcome()
        self.battle()
        self.show_winner()

    def welcome(self):
        print('Welsome to Robots vs Dinosaurs')
    
    def get_random_number(ran_number):
        return random.choice(ran_number)
    
    def battle():
        while len(self.herd.Dinosaurs) > 0 and len(self.fleet.robots) > 0:
            
""" 
def __init__(self):
    self.run_game 
display_welcome(self): void
battle(self): void
dino_turn(self, Dinosaur): void
robo_turn(self, Robot): void
show_dino_opponent_option(self): void
show_robo_opponent_option(self): void
display_winner(self): void
 """