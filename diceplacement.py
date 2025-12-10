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
        Creates variables:
            placement_dict (dict): dictionary containing the die values from the
                                dice list as keys and possible placement locations
                                as values
            prompt_list (list of lists): die values that have more than one 
                                        placement option
            bury_dice (list of ints): list of die values determined to be placed
                                    in the player's yard
        Updates the Card obj attributes req_dice and yard
    Returns:
        bust_test (bool): True/False returned by bust function
        
    Author: Mackenzie Barrett
    Technique: Sequence Unpacking
    """
    
    # Print dice list to the player
    print(f"Your rolled dice are: {dice_list}")
    # Print active cards to the player and their yard
    print("Your current active dog cards are:\n")
    for card in player.active_cards:
        print(f"{card}\n")
    print(f"Your yard: {player.yard}\n")
    # Ask player which card they would like to place the first die in the dice list in
        # if they cannot put it on a card they should select their yard
        # check if the player busts
    for die in dice_list:
        card_choice = input(f"\nEnter the name of the card you would like to "\
            f"place the {die} on (if you have no place to put the die, enter"\
                f" the word yard): ")
        if card_choice == 'yard':
            player.yard.append(die)
            bust_test = bust(player)
            return bust_test
        else:
            for card in player.active_cards:
                if card.name == card_choice:
                    card.req_dice[die] = True
                    