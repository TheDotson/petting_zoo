from alligator import Alligator
from arapaima import Arapaima
from copperhead import Copperhead
from dart_frog import Dart_Frog
from donkey import Donkey
from duck import Duck
from goat import Goat
from goldfish import Goldfish
from horse import Horse
from llama import Llama
from manatee import Manatee
from pig import Pig
from rat_snake import Rat_Snake
from salamander import Salamander
from snapping_turtle import Snapping_Turtle

from attractions import PettingZoo, Herpetarium, RiverExhibit


def main():

  varmint_village = PettingZoo("Varmint Village")
  tropical_wonders = Herpetarium("Tropical Wonders")
  river_life = RiverExhibit("River Life")


  #River
  drake = Duck("Drake", "Mallard", "bread")
  river_life.add_animal(drake)

  ari = Arapaima('Ari', 'Pirarucu', 'fish')
  river_life.add_animal(ari)

  steve = Snapping_Turtle('Steve', 'Alligator Snapping Turtle', 'fish')
  river_life.add_animal(steve)


  #Petting Zoo
  keith = Donkey('Keith', 'Standard Donkey', 'noon', 'carrots')
  print(f'{keith.name} the {keith.species} is available to pet during {keith.shift}.')
  varmint_village.add_animal(keith)

  bryan = Llama("Bryan", "Domestic Llama", "morning", "Llamas")
  varmint_village.add_animal(bryan)

  bucephalus = Horse("Bucephalus", "Appaloosa", "afternoon", "oats")
  varmint_village.add_animal(bucephalus)


  #Herpetarium
  leon = Alligator('Leon', 'American', "chicken", 12345)
  print(leon.feed())
  print(leon.chip_number)
  tropical_wonders.add_animal(leon)

  lenny = Dart_Frog('Lenny', 'Strawberry Poison', 'flies')
  tropical_wonders.add_animal(lenny)

  mark = Copperhead('Mark', 'Copperhead', 'mice')
  tropical_wonders.add_animal(mark)

  varmint_village.get_animals()
  tropical_wonders.get_animals()
  river_life.get_animals()
  print("Last Varmint added:", varmint_village.last_critter_added)
  print("Last Wonder added:", tropical_wonders.last_critter_added)
  print("Last Denizen added:", river_life.last_critter_added)

main()
