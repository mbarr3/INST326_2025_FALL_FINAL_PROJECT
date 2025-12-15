from random_roll import roll
from diceplacement import dice_placement

def fetch(player, total_rolls):
    """Function to represent the "Fetch" action in the Spots game. 
    
    Roll 8 dice. Choose a number you rolled, and place or bury all dice of that 
    number. Discard the rest.
    
    Args:
        player (Player obj): a Player class object with access to Player
            attributes for the dice_placement function
        total_rolls (list): list of all dice rolled throughout the game
    Side effects:
        Prints rolled dice to terminal
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable
        Prints input prompt to terminal asking which value the player wants
        Prints players selected dice list to the terminal
        Adds rolled dice to total_rolls
    Returns:
        bust_test (bool): True or False as returned by the bust function

    Author: Mackenzie Barrett
    Technique: List Comprehension
    """
    while True:
        # Call roll function and save returned list to a variable
        rolled = roll(8)
        reroll = None
        
        print(f"\nRolled dice: {rolled}")
        
        if player.treats > 0:
            while True:
                reroll = input(f"You have {player.treats} treat(s). Would you "\
                    f"like to spend a treat to reroll? (y/n) ").lower()
                if reroll not in ['yes', 'y', 'no', 'n']:
                    print(f"{reroll} is not y or n")
                    continue
                else:
                    break
        
        # Restart function if they want to spend a treat  
        if reroll == "y" or reroll == "yes":
            player.treats-=1
            continue
        
        total_rolls.extend(rolled)
        
        # Prompt and validate user input
        while True:
            chosen_num = input("\nChoose one of the numbers present in the " 
                            "rolled dice(you will have to place or bury all "
                            "dice of that number): ")
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