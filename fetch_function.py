import random_roll
    

def fetch():
    """Function to represent the "Fetch" action in the Spots game. Fetch calls the 
    future dice_roll function with an arg of 8 so it returns a list of 8 rolled dice.
    Prompts the player to select a number from the rolled dice and validates that
    input.

    Side-effects:
        Saves the list returned by the dice_roll function to a variable
        Creates a chosen_num variable to store the player's input chosen number
    
    Returns:
        A list of the rolled die that are the number input by the player
        
    Author: Mackenzie Barrett
    Technique: List Comprehension
    """
    # Call temporary dice_roll function and save returned list to a variable
    rolled = random_roll(8)
    print(f"Rolled dice: {rolled}")
    # Prompt and validate user input
    while True:
        chosen_num = input("Choose one of the numbers present in the rolled dice" 
                           "(you will have to place or bury all dice of that "
                           "number): ")
        if isinstance(chosen_num, int):
            if chosen_num in range(1,7):
                if chosen_num in rolled:
                    break
        else:
            print(f"{chosen_num} is not present in the rolled dice")
            continue
        
    return [die for die in rolled if die == chosen_num]
            
