# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
        self.in_hand = ""


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
                print(f"{item[0]} has been added to your backpack.") 
        else:
            print("There is nothing of interest in this room.")

    def get_item(self):
        item = input("*Which item would you like to get from your backpack?* ")
        if str(item) in str(self.items):
            print(item, str(self.items), "ITEMS")
            # print(self.in_hand)
            # self.items.remove(str(item))
            print(f"You wield the {self.in_hand} in your hand")
        else:
            print("You don't have that item in your backpack.")
            
    def drop_item():
        item = input("*Which item would you like to drop?* ")
        if str(item) in str(self.items):
            self.location.dropped_items.append(item)
            print(f"{item} has been dropped.")
            print(self.location.dropped_items)
