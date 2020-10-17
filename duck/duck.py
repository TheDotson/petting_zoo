from datetime import date

class Duck:
  def __init__(self, name, species, shift):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True
    self.shift = shift
