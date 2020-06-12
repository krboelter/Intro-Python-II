# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []


    def __str__(self):
        return f"{self.name}"

    def search_room(self):
        if self.location.furniture is not None:
            self.location.show_furniture()

            # to optimize, add try, catch for character outside of scope
            search = input("\n*Which item would you like to search?* ")
            
            if int(search) in range(1, len(self.location.furniture) + 1):
                item = self.location.furniture[int(search) - 1].contents
                self.items.append(item)
                print(f"You picked up: {item[0]}.") 
        else:
            print("There is nothing of interest in this room.")
            
