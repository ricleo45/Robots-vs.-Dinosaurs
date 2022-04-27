from robot import Robot
class Fleet:
    def __init__(self):
      self.robots = []
      self.robot_list()
 
    def robot_list(self):
        robot1 = Robot('Toaster')
        robot2 = Robot('Vacuum')
        robot3 = Robot('Dishwasher')

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
