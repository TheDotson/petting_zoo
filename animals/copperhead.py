from .animal import Animal
from datetime import date
from movements import Slithering

class Copperhead(Animal, Slithering):
  def __init__(self, name, species, food, chip_num):
    Animal.__init__(self, name, species, food, chip_num)
    Slithering.__init__(self)
