class Dinosaur: 
    def __init__(self, dino_name, dino_attack_power):

        self.name = dino_name
        self.health = 100
        self.attack_power = dino_attack_power

    def attack(self, Robot):
        Robot.health = Robot.health - self.attack_power
        print(f'{Robot.health} is down :{Robot.health}!!!')
