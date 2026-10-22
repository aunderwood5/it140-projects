"""Module Six Milestone starter for the simplified movement prototype."""

# Anna Underwood
# IT-140 Module Six Milestone
# Simplified Dragon Text Game


# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}


# Set the player's starting room.
current_room = 'Great Hall'


# Continue the game until the player chooses to exit.
while current_room != 'exit':

    # Display the player's current room.
    print('You are in the', current_room)

    # Prompt the player to enter a command.
    command = input('Enter your move: ').lower().strip()

    # Check if the player wants to exit.
    if command == 'exit':
        current_room = 'exit'

    # Check for a movement command.
    elif command.startswith('go '):
        direction = command[3:]

        # Move to the new room if the direction is valid.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    # Handle invalid commands.
    else:
        print('Invalid command!')


# End the game.
print('Thanks for playing!')
