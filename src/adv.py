from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main


# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Ken", room['outside'])
print(player_1.location)

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    user_input = input("\n*Which direction would you like to go?* ")

    try:
        if user_input == "n" or user_input == "N":
            if player_1.location.n_to:
                player_1.move_to(player_1.location.n_to)
        elif user_input == "e" or user_input == "E":
            if player_1.location.e_to:
                player_1.move_to(player_1.location.e_to)
        elif user_input == "s" or user_input == "S":
            if player_1.location.s_to:
                player_1.move_to(player_1.location.s_to)
        elif user_input == "w" or user_input == "W":
            if player_1.location.w_to:
                player_1.move_to(player_1.location.w_to)
        elif user_input == "q" or user_input == "Q":
            print("Thanks for playing!")
            break
        else:
            print("Not a valid command")
    except:
        print("No room in that direction")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


