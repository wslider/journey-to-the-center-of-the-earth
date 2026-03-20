import math

def main():

    def setup_player():
        name = ""
        while not name:  # keeps going while name is empty
            name = input("Enter your name: ").strip()
            if not name:
                print("Please enter a name – you can't start without one!")
        
        print(f"Welcome, {name}! You are ready to descend into the depths of the unknown.")
        
        return {
            'name': name,
            'health': 100,
            'inventory': {},
            'companions': {},
            'places': []
        }
    
    # set up artifacts
    # set up places 
    # set up companions
    # check stats
    # end game 
    # run game loop 
    
    player = setup_player()
    print("\nYour character has been created:")
    print(player)

if __name__ == "__main__":
    main()