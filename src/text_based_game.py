"""Project Two Text-Based Adventure Game."""

# Anna Underwood


def show_instructions():
    """Display the game objective and available commands."""
    print("Escape the Haunted Hotel")
    print("Collect all 6 items before entering the basement to escape!")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get 'item name'")
    print()


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    # Display the item in the room if it has not been collected.
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        if item not in inventory:
            print("You see a", item)

    print("---------------------------")


def main():
    """Run the main gameplay loop."""

    # Dictionary connects the rooms and items in the Haunted Hotel.
    rooms = {
        "Hotel Lobby": {
            "west": "Dining Room"
        },
        "Dining Room": {
            "north": "Guest Room",
            "east": "Hotel Lobby",
            "item": "Flashlight"
        },
        "Guest Room": {
            "north": "Kitchen",
            "south": "Dining Room",
            "east": "Basement",
            "item": "First Aid Kit"
        },
        "Kitchen": {
            "south": "Guest Room",
            "east": "Laundry Room",
            "item": "Key"
        },
        "Laundry Room": {
            "west": "Kitchen",
            "east": "Manager's Office",
            "south": "Basement",
            "item": "Rope"
        },
        "Manager's Office": {
            "west": "Laundry Room",
            "south": "Security Room",
            "item": "Master Key"
        },
        "Security Room": {
            "north": "Manager's Office",
            "west": "Basement",
            "item": "Security Badge"
        },
        "Basement": {
            "north": "Laundry Room",
            "east": "Security Room",
            "west": "Guest Room"
        }
    }

    # Set the player's starting room and inventory.
    current_room = "Hotel Lobby"
    inventory = []

    # Display the game instructions.
    show_instructions()

    # Continue gameplay until the player wins or loses.
    while True:
        show_status(current_room, inventory, rooms)

        # Check whether the player has entered the villain's room.
        if current_room == "Basement":
            if len(inventory) == 6:
                print("Congratulations! You collected all 6 items")
                print("and defeated the Haunted Hotel Keeper!")
                print("You escaped the Haunted Hotel!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("The Haunted Hotel Keeper found you!")
                print("GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # Ask the player for the next command.
        command = input("Enter your move: ").strip()

        # Handle movement commands.
        if command.lower().startswith("go "):
            direction = command[3:].lower()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Handle commands for collecting items.
        elif command.lower().startswith("get "):
            requested_item = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if requested_item.lower() == room_item.lower():
                    if room_item not in inventory:
                        inventory.append(room_item)
                        print(room_item, "retrieved!")
                    else:
                        print("You already have the", room_item + ".")
                else:
                    print("Can't get", requested_item + "!")
            else:
                print("There is no item to collect in this room.")

        # Handle invalid commands.
        else:
            print("Invalid Input!")


# Run the game.
if __name__ == "__main__":
    main()
