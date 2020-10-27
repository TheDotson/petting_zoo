from .animal import Animal
from datetime import date
from movements import Walking

class Llama(Animal):
  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, food, chip_num)
    Walking.__init__(self)
    self.walking = False
    self.shift = shift
