print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input("You're at a crossroad. Where do you want to go?\n\tType 'left' or 'right': ").capitalize()

if direction == "Left":
    action = input("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across: ").capitalize()

    if action == "Wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?: ").capitalize()

        if door == "Red":
            print("It's a room full of fire. GAME OVER!")
        elif door == "Blue":
            print("You enter a room of beasts. GAME OVER!")
        elif door == "Yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. GAME OVER!")
    else:
        print("You get attacked by an angry trout. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")