from weapons import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.rodo_health = 100
        self.weapon = Weapon('sword', 25)

    def attack(self, Dinosaur):
        Dinosaur.health -= self.weapon.attack_power
        print(f'{Dinosaur.name} is down :{Dinosaur.health} !!!')


