from datetime import date

class Copperhead:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.slithering = True
