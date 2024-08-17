from island import island_scenario

def lake_scenario():
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: ')
    if choice2 == "wait":
        print("You wait for a boat. A boat arrives and takes you to the island.")
        island_scenario()
    elif choice2 == "swim":
        print("You swam across the lake but got eaten by a shark. Game Over.")
    else:
        print("Invalid choice. Game Over.")
