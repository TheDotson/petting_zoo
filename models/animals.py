from datetime import date

#petting zoo
class Donkey:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True

keith = Donkey('Keith', 'Standard')
print(keith)

class Llama:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True

bryan = Llama('Bryan', 'Domestic')
print(bryan)

class Goat:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True

tina = Goat('Tina', "Mountain")
print(tina)

class Pig:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True

joe = Pig('Joe', 'American Yorkshire')
print(joe)

class Horse:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.walking = True

bucephalus = Horse('Bucephalus', 'Appaloosa')
print(bucephalus)



#herpetarium
class Copperhead:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.slithering = True

mark = Copperhead('Mark', 'Copperhead')
print(mark)

class Rat_Snake:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.slithering = True

drew = Rat_Snake('Drew', 'Rat Snake')
print(drew)

class Alligator:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True

leon = Alligator('Leon', 'American')
print(leon)

class Salamander:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True

susan = Salamander('Susan', 'Axolotl')
print(susan)

class Dart_Frog:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True

lenny = Dart_Frog('Lenny', 'Strawberry Poison')
print(lenny)



#river_exhibit
class Duck:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True

drake = Duck('Drake', 'Mallard')
print(drake)

class Goldfish:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True

lil_dude = Goldfish('Drake', 'Black Moor')
print(lil_dude)

class Arapaima:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True

ari = Arapaima('Ari', 'Pirarucu')
print(ari)

class Snapping_Turtle:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True

steve = Snapping_Turtle('Steve', 'Alligator')
print(steve)

class Manatee:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.data_added = date.today()
    self.walking = True
    self.swimming = True
    self.flying = True

ana = Manatee('Ana', 'American')
print(ana)
