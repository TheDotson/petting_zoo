from .attraction import Attraction
from movements import Swimming

class RiverExhibit(Attraction):
  def __init__(self, name, description):
    super().__init__(name, description)

  def add_animal_type_check(self, animal):
    if isinstance(animal, Swimming):
      self.animals.append(animal)
      print(f"{animal} now lives in the {self.name}")
    else:
      print(f"{animal} doesn\'t like to be wet, so please do not put them in the {self.name} attraction.")
