from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot('Beeper')
        robot2 = Robot('Clicker')
        robot3 = Robot('Bopper')

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)

