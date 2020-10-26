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


def main():
  keith = Donkey('Keith', 'Standard Donkey', 'noon', 'carrots')
  print(f'{keith.name} the {keith.species} is available to pet during {keith.shift}.')

  bryan = Llama("Bryan", "Domestic Llama", "morning", "Llamas")
  print(bryan.feed())

  bucephalus = Horse("Bucephalus", "Appaloosa", "afternoon", "oats")
  print(bucephalus.feed())

main()
