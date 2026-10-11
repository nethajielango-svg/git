import os

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")