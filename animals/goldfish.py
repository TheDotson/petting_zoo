from animals import Animal
from datetime import date

class Goldfish(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.swimming = True
