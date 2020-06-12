# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.furniture = []

    def __str__(self):
        return f"You are currently in the {self.name}, it is {self.description}."

    def show_furniture(self):
        if self.furniture is not None:
            print("Furniture in the room:")
            for i in range(len(self.furniture)):
                print(f"{i + 1}: {self.furniture[i]}.")
        else:
            print("There is nothing of interest in this room")

