class Weapon:
    
    def __init__(self, name, attack_power):
        self.name = name
        self.power = attack_power

    def __str__(self) -> str:
        return f'using {self.name}'

hammer = Weapon('Hammer', 25)
sword = Weapon('Sword', 25)
laser = Weapon('Laser', 25)
