from lake import lake_scenario

def start_game():
    print('''
    o            o
     \          /
      \        /
       :-'""'-:
    .-'  ____  `-.
   ( (  (_()_)  ) )
    `-.   ^^   .-'
       `._==_.'
        __)(___
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice1 = input('You are at a crossroad, where do you want to go? Type "left" or "right": ')

    if choice1 == "left":
        lake_scenario()
    else:
        print("You fell into a hole. Game Over.")

if __name__ == "__main__":
    start_game()
