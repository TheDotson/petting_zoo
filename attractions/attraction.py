class Attraction:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def get_animals(self):
        print(f"{self.name} is where you'll find {self.description}, like:")
        for animal in self.animals:
            print(
                f'\t* {animal.name} the {animal.species}')

    def __str__(self):
        return (f"{self.name} ({len(self)} animals)")

    def __len__(self):
        return len(self.animals)

    @property  # getter
    def last_critter_added(self):
        return f'\t* {self.animals[-1].name} the {self.animals[-1].species}'
