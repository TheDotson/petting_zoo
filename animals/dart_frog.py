from animals import Animal
from datetime import date

class Dart_Frog(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.slithering = True
