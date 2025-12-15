from bust import bust 

def dice_placement(player, dice_list):
    """Prompts the player to place the dice in the dice list to either an active
        card they have or their yard
        
    Args:
        player (Player class obj): Player class object to provide active_cards
                                    list
        dice_list (list of ints): list of dice values that need to either be 
                                placed automatically or by the player if more
                                than one option is available
    Side effects:
        Prints active dog cards message and card objs __str__ to the terminal
        Prints player yard attribute to the terminal
        Prints input to terminal asking which card or yard they would like to 
            place the prompted die on
        If input error prints error message to the terminal
        Updates the Card obj attributes req_dice and yard
    Returns:
        bust_test (bool): True/False as returned by bust function
        
    Author: Mackenzie Barrett
    """
    
    for die in dice_list:
        # Print active cards to the player and their yard
        print("\nYour current active dog cards are:\n")
        for card in player.active_cards:
            print(f"{card}\n")
        print(f"Your yard: {sum(player.yard)}\n")
        
        # Ask player which card they would like to place the first die in the dice list in
        # if they cannot put it on a card they should select their yard
        while True:
            card_choice = input(f"Enter the name of the card you would like to "\
                f"place the {die} on (if you have no place to put the die, enter"\
                    f" the word yard): ")
            if card_choice.lower() == 'yard':
                player.yard.append(die)
                # check if the player busts
                bust_test = bust(player)
                if bust_test == True:
                    return bust_test
                else:
                    break
            else:
                found = False
                for card in player.active_cards:
                    if card.name == card_choice.lower().capitalize() and die in card.req_dice.keys():
                        if card.req_dice[die] == False: 
                            card.req_dice[die] = True 
                            found = True
                if found == False:
                    print ("\nInvalid Selection: either the card you chose"\
                        " was not found or does not have a spot for the die "\
                            "value you selected")
                    continue
                else:
                    break
    return False     