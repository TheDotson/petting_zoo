from .attraction import Attraction
from movements import Slithering

class Herpetarium(Attraction):
  def __init__(self, name, description):
    super().__init__(name, description)

  def add_animal_type_check(self, animal):
    if isinstance(animal, Slithering):
      self.animals.append(animal)
      print(f"{animal} now lives in {self.name}")
    else:
      print(f"{animal} doesn\'t like to be in the warm climate, so please do not put them in the {self.name} attraction.")
