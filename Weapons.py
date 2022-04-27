class Weapon:
    
    def __init__(self, name, attack_power):
        self.name = name
        self.power = attack_power

    def __str__(self) -> str:
        return f'using a {self.name}'

hammer = Weapon('Toast', 25)

print(hammer)