from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur('Giant Chicken', 50)
        dinosaur2 = Dinosaur('Lizard', 50)
        dinosaur3 = Dinosaur('Crocodile', 50)

        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)