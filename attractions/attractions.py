class PettingZoo:

  def __init__(self, name):
    self.attraction_name = name
    self.description = "cute and fuzzy critters to cuddle"
    self.animals = list()

  def add_animal(self, animal):
    self.animals.append(animal)

  def get_animals(self):
    print(f"{self.attraction_name} is where you'll find {self.description}, like:")
    for animal in self.animals:
      print(f'\t* {animal.name} the {animal.species}')

class Herpetarium:

  def __init__(self, name):
    self.attraction_name = name
    self.description = "reptilian and amphibious wonders"
    self.animals = list()

  def add_animal(self, animal):
    self.animals.append(animal)

  def get_animals(self):
    print(f"{self.attraction_name} is where you'll find {self.description}, like:")
    for animal in self.animals:
      print(f'\t* {animal.name} the {animal.species}')



class RiverExhibit:

  def __init__(self, name):
    self.attraction_name = name
    self.description = "the fantastic denizens of the river system"
    self.animals = list()

  def add_animal(self, animal):
    self.animals.append(animal)

  def get_animals(self):
    print(f"{self.attraction_name} is where you'll find {self.description}, like:")
    for animal in self.animals:
      print(f'\t* {animal.name} the {animal.species}')
