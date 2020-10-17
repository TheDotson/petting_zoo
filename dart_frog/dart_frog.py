from datetime import date

class Dart_Frog:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.swimming = True
