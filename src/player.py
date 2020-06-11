# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []


    def __str__(self):
        return f"{self.name}"


    def move_to(self, direction):
        self.location = direction
        print(f"{self.location}")
