# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
        self.in_hand = []

    def __str__(self):
        return f"{self.name}"

    def search_room(self):
        if self.location.furniture is not None:
            self.location.show_furniture()

            # to optimize, add try, catch for character outside of scope
            search = input("\n*Which item would you like to search?* ")

            try:
                if int(search) in range(1, len(self.location.furniture) + 1):
                    item = self.location.furniture[int(search) - 1].contents
                    self.items.append(item)
                    print(f"{item[0]} has been added to your backpack.") 
            except:
                print("Not a valid command")
        else:
            print("There is nothing of interest in this room.")

    def get_item(self):
        item = input("*Which item would you like to get from your backpack?* ")
        
        # check to see if player has the item
        if item in str(self.items):

            # remove the item from self.items array
            for i in range(len(self.items)):
                if self.in_hand:
                    self.items.append(self.in_hand)
                    self.in_hand = []
                if item == self.items[i][0]:
                    self.in_hand = self.items[i]
                    self.items.remove(self.items[i])
            print(f"You wield the {self.in_hand[0]} in your hand")
        else:
            print("You don't have that item in your backpack.")
            
    def drop_item(self):
        item = input("*Which item would you like to drop?* ")
        if item in str(self.items) or item in str(self.in_hand):
            self.location.dropped_items.append(item)
            print(f"{item} has been dropped.")
            for i in range(len(self.items)):
                self.items.remove(self.items[i])
        else:
            print("You do not own that item")

