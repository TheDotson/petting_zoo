from animals import Duck, Turtle, Llama, Arapaima, Donkey, Horse, Alligator, Dart_Frog, Copperhead
from attractions import PettingZoo, Herpetarium, RiverExhibit


def main():

  varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
  tropical_wonders = Herpetarium("Tropical Wonders", "reptilian and amphibious wonders")
  river_life = RiverExhibit("River Life", "the fantastic denizens of the river system")


  #River
  drake = Duck("Drake", "Mallard", "bread", 123)
  river_life.add_animal_type_check(drake)

  ari = Arapaima('Ari', 'Pirarucu', 'fish', 456)
  river_life.add_animal_type_check(ari)

  steve = Turtle('Steve', 'Alligator Snapping Turtle', 'fish', 789)
  river_life.add_animal_type_check(steve)


  #Petting Zoo
  keith = Donkey('Keith', 'Standard Donkey', 'noon', 'carrots', 101112)
  print(f'{keith.name} the {keith.species} is available to pet during {keith.shift}.')
  varmint_village.add_animal_type_check(keith)

  bryan = Llama("Bryan", "Domestic Llama", "morning", "Llamas", 131415)
  varmint_village.add_animal_type_check(bryan)

  bucephalus = Horse("Bucephalus", "Appaloosa", "afternoon", "oats", 171819)
  varmint_village.add_animal_type_check(bucephalus)
  
  leon = Alligator('Leon', 'American Alligator', "chicken", 202122)
  varmint_village.add_animal_type_check(leon)



  #Herpetarium
  leon = Alligator('Leon', 'American Alligator', "chicken", 202122)
  print(leon.feed())
  print(leon.chip_number)
  tropical_wonders.add_animal_type_check(leon)

  lenny = Dart_Frog('Lenny', 'Strawberry Poison Frog', 'flies', 232425)
  tropical_wonders.add_animal_type_check(lenny)

  mark = Copperhead('Mark', 'Copperhead', 'mice', 262728)
  tropical_wonders.add_animal_type_check(mark)

  varmint_village.get_animals()
  tropical_wonders.get_animals()
  river_life.get_animals()
  print("Last Varmint added:", varmint_village.last_critter_added)
  print("Last Wonder added:", tropical_wonders.last_critter_added)
  print("Last Denizen added:", river_life.last_critter_added)

main()
