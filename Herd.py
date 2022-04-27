from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
      self.Dinosaur = []
      self.dino_list()
 
    def dino_list(self):
        dino1 = Dinosaur('t-rex', 50)
        dino2 = Dinosaur('velociraptor', 50)
        dino3 = Dinosaur('giant-chicken', 50)

        self.Dinosaur.append(dino1)
        self.Dinosaur.append(dino2)
        self.Dinosaur.append(dino3)

