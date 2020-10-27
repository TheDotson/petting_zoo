from .attraction import Attraction

class Herpetarium(Attraction):
  def __init__(self, name, description):
    super().__init__(name, description)

  def add_animal_pythonic(self, animal):
    try:
      if animal.slither_speed > -1:
        self.animals.append(animal)
        print(f"{animal} now lives in {self.attraction_name}")
    except AttributeError as ex:
      print(f"{animal} doesn\'t like to be in the warm climate, so please do not put them in the {self.attraction_name} attraction.")