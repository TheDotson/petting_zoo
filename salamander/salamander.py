from datetime import date

class Salamander:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.swimming = True
    self.food = food

  def feed(self):
    return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

  def __str__(self):
    return f"My name is {self.name} and I am a {self.species}"
