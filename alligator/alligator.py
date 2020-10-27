from datetime import date

class Alligator:
  def __init__(self, name, species, food, chip_num):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.swimming = True
    self.food = food
    self.__chip_num = chip_num #privately scoped atrribute

  def feed(self):
    return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

  def __str__(self):
    return f"My name is {self.name} and I am a {self.species}"

  @property #getter
  def chip_number(self):
    return self.__chip_num

  @chip_number.setter #setter
  def chip_number(self, number):
    pass
