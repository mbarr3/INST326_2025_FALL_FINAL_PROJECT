from random_roll import roll as rr
from diceplacement import dice_placement as dp

def trot(player, total_rolls):
    """Function for the trot trick

    You may move 1 die on your dog cards to any other space, changing the number if 
    needed
    THEN 
    Roll 2 dice

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
        total_rolls (list): list of all dice rolled throughout the game
    Side effects:
        Prints the player's active cards to the terminal
        Prompts the player to input which card they would like to remove a die 
            from, which die to remove, which card to place the die on, and what
            value to set the die to
            Skip input possible to skip this part
        Updates card obj attributes accordingly
        If applicable, prints input error message to terminal
        Prints info message to player that they will roll 2 dice
        Prints rolled die 
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable
        Adds rolled dice to total_rolls
    Returns:
        bust_test (bool): True or False as returned by the bust function
        
    Author: Samuel Onakoya
    Technique: Keyword arguments
    """
    
    while True:
        # Print active cards to the player and their yard
        print("Your current active dog cards are:\n")
        for card in player.active_cards:
            print(f"{card}\n")
        print(f"Your yard: {sum(player.yard)}\n")
        old_card = input("\nEnter the name of the card you would like to remove"\
            " a die from (or type 'skip'): ")
        
        # Allow skip
        if old_card.lower() == 'skip':
            break
        
        old_value = int(input("which die value would like to remove? "))
        
        found = False
        
        for card in player.active_cards:
            if card.name.lower() == old_card.lower() and old_value in card.req_dice.keys():
                if card.req_dice[old_value] == True:
                    card.req_dice[old_value] = False
                    found = True
        if found == False:
            print("Invalid selection: Either the card you selected was not "\
                "found or does not have the fulfilled die value you selected")
            continue
        else:
            break
        

    
    # Only do die placement if not skipped
    if old_card.lower() != 'skip':
        while True:
            new_value = int(input("Choose a new value for this die(1-6): "))
            
            try:
                new_value = int(new_value)    
            except:
                print("\nInvalid Selection: You did not enter a number value.")
                continue
                
            if new_value in range(1,7):
                break
            else:
                print(f"\nInvalid Selection: {new_value} is not a number between 1 and 6")
                continue
        
        bust_test = dp(player, [new_value]) 
        if bust_test == True:
            return bust_test

    print("\n***~~~Now you roll two dice~~~***")
    while True:
        dice = rr(rolls = 2)
        reroll = None
        print(f"\nYour rolled dice are: {dice}")
        if player.treats > 0:
                while True:
                    reroll = input(f"You have {player.treats} treat(s). Would you like to spend "\
                        f"a treat to reroll? (y/n) ").lower()
                    if reroll not in ['yes', 'y', 'no', 'n']:
                        print(f"{reroll} is not y or n")
                        continue
                    else:
                        break
                    
        if reroll == "y" or reroll == "yes":
                player.treats -= 1
                continue
        
        bust_test = dp(player, dice)
        return bust_test