print("Welcome to Treasure Island. \nYour mission is to find the treasure")
crossroad = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if crossroad.lower() == "right":
    print(f"You chose {crossroad.lower()}. You were attacked by rogue pirates. Game Over.")
elif crossroad.lower() == "left":
    print(f"You chose {crossroad.lower()}. You walk to a small lake.")
    swim_or_wait = input("Do you swim or wait for a boat? Type 'swim' or 'wait' ")
    if swim_or_wait.lower() == "swim":
        print("You chose to swim. You were eaten by hungry crocodiles. Game Over.")
    elif swim_or_wait.lower() == "wait":
        print(
            "You chose to wait. A ferryman came by, to take you to the island.\nNow on the island, you walk into a cave. ")
        door_color = input("The cave has three doors, which one do you choose? Red, yellow, or blue ")
        if door_color.lower() == "red":
            print(
                f"You chose the {door_color} door. When opening the door, an explosion went off, and you died. Game Over.")
        elif door_color.lower() == "yellow":
            print(
                f"You chose the {door_color} door. Upon opening the door, you discover a room filled with treasure. You Win!")
        elif door_color.lower() == "blue":
            print(
                f"You chose the {door_color} door. Opening the door set off a trap, and arrows pierced through you. Game Over.")
