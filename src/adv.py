from room import Room
from player import Player
from furniture import Furniture

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Create furniture

dresser = Furniture("dresser", "A wooden dresser, looks like its been here a while", [])
sofa = Furniture("sofa", "A large sofa. There are almost definitely things between the cushions", [])
desk = Furniture("desk", "Used for doing work.", [])
table = Furniture("table", "Used for hosting banquets and feasts", [])
chest = Furniture("chest", "Used for storing personal treasures", [])

# Assign furniture

room['foyer'].furniture = [dresser, sofa]
room['treasure'].furniture = [chest, desk, table]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Create items

candle = ("candle", "Helpful in the dark... or for a small amount of warmth")
key = ("key", "A well-polished, silver key")
note = ("handwritten note", "The note reads: You are too late, the treasure is mine... Cpt. Drax Maygar")


# Assign items

sofa.contents = key
dresser.contents = candle
chest.contents = note

# Main

player_1 = Player("Ken", room['outside'])
print(player_1.location)

while True:
    user_input = input("\n*What would you like to do?* ")

    if user_input in ["n", "e", "s", "w", "q", "search", "get", "drop"]:
        if hasattr(player_1.location, f"{user_input}_to"):
            player_1.location = getattr(player_1.location, f"{user_input}_to")
            print(player_1.location)
        elif user_input == "search":
            player_1.search_room()
        elif user_input == "get":
            player_1.get_item()
        elif user_input == "q":
            print("Thanks for playing!")
            break
        else:
            print("Not a valid command")

