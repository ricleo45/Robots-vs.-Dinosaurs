from dinosaur import Dinosaur

class Herd:
    def __init__(self):
      self.Dinosaur = []
      self.dino_list()
 
    def dino_list(self):
        dino1 = Dinosaur('t-rex')
        dino2 = Dinosaur('velociraptor')
        dino3 = Dinosaur('giant-chicken')

        self.Dinosaur.append(dino1)
        self.Dinosaur.append(dino2)
        self.Dinosaur.append(dino3)