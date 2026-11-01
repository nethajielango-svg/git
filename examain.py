import os


class main():
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Only instances of Animal can be added.")

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name} is a {animal.species}.")