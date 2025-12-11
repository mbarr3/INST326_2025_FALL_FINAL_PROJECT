from random_roll import roll
from diceplacement import dice_placement

def fetch(player, total_rolls):
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
    while True:
        # Call roll function and save returned list to a variable
        rolled = roll(8)
        total_rolls.extend(rolled)
        reroll = None
        
        print(f"\nRolled dice: {rolled}")
        
        if player.treats > 0:
            while True:
                reroll = input(f"You have {player.treats} treat(s). Would you like to spend "\
                    f"a treat to reroll? (y/n) ").lower()
                if reroll not in ['yes', 'y', 'no', 'n']:
                    print(f"{reroll} is not y or n")
                    continue
                else:
                    break
        
        # Restart function if they want to spend a treat  
        if reroll == "y" or reroll == "yes":
            player.treats-=1
            continue
        
        # Prompt and validate user input
        while True:
            chosen_num = input("\nChoose one of the numbers present in the rolled dice" 
                            "(you will have to place or bury all dice of that "
                            "number): ")
            try:
                chosen_num = int(chosen_num)
            except:
                print("\nInvalid Selection: You did not enter a number value.")
                continue
                
            if isinstance(chosen_num, int):
                if chosen_num in range(1,7):
                    if chosen_num in rolled:
                        break
            else:
                print(f"Invalid Selection: {chosen_num} is not present in the "\
                    "rolled dice")
                continue
        
        dice_list = [die for die in rolled if die == chosen_num]
        
        print(f"\nYour dice list is: {dice_list}")
        
        bust_test = dice_placement(player, dice_list)
        return bust_test