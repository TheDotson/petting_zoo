from animals import Animal
from datetime import date
from movements import Slithering

class Copperhead(Animal):
  def __init__(self, name, species, food, chip_num):
    super().__init__(name, species, food, chip_num)
    Slithering.__init__(self)
    self.slithering = False
