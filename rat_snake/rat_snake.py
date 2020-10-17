from datetime import date

class Rat_Snake:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.slithering = True
