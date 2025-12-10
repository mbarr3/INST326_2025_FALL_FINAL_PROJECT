from random_roll import roll
from diceplacement import dice_placement

def fetch(player):
    """Function to represent the "Fetch" action in the Spots game. Fetch calls the 
    random_roll function with an int arg so it returns a list of int rolled dice.
    Prompts the player to select a number from the rolled dice and validates that
    input. Creates a list of all the die with the selected value. Passes that list
    to the dice placement function. 
    
    Args:
        player (Player obj): a Player class object with access to Player
            attributes for the dice_placement function
    Side effects:
        Calls roll function
        Saves the list returned by the roll function to a variable
        Prints the list to the terminal
        Creates a chosen_num variable to store the player's input chosen number
        Calls dice placement function 
    Returns:
        bust_test (bool): True or False to indicate if the player's turn should end

    Author: Mackenzie Barrett
    Technique: List Comprehension
    """
    # Call temporary dice_roll function and save returned list to a variable
    rolled = roll(8)
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
    
    bust_test = dice_placement(player, [die for die in rolled if die == chosen_num])
    if bust_test == True:
        return bust_test
    
