from .attraction import Attraction
from movements import Walking

class PettingZoo(Attraction):
  def __init__(self, name, description):
    Attraction.__init__(self, name, description)
    
  def add_animal_type_check(self, animal):
    if isinstance(animal, Walking):
      self.animals.append(animal)
      print(f"{animal} now lives in {self.name}")
    else:
      print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.name} attraction.')
