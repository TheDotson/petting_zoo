from .animal import Animal
from datetime import date
from movements import Swimming, Slithering

class Alligator(Animal, Swimming, Slithering):
  def __init__(self, name, species, food, chip_num):
    Animal.__init__(self, name, species, food, chip_num)
    Swimming.__init__(self)
    Slithering.__init__(self)
