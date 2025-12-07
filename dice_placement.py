import bust


def dice_placement(player, dice_list):
    """Takes a list of dice values and determines if they can be placed on any
    active dog cards. If there is more than one available spot to place the die
    it prompts the player to choose which card other wise it automatically fills
    the one available spot. If there are no available spots for the die value 
    the die is automatically placed in the player's yard and the bust function 
    is called. 
    
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

    Returns:
    
    Author: Mackenzie Barrett
    Technique: 
    """
    placement_dict = {}
    prompt_list = []
    bury_dice = []
    
    # Check for possible placement spots for each die value in the dice list
    for die in dice_list:
        placement_dict[die] = set()
    for key in placement_dict.keys():
        for card in player.active_cards:
            for die in card.req_dice.keys():
                if card.req_dice[key] == None:
                    placement_dict[key].add(card)
    
    # Place die automatically on a card or in the yard OR prompt player to choose placement if multiple options   
    for key in placement_dict.keys():
        # Place any values with multiple placement options in a list
        if len(placement_dict[key]) > 1:
            prompt_list.append(key)
        # Automatically place die values on a card if only one placement is available
        elif len(placement_dict[key]) == 1:
            open_card = placement_dict[key]
            open_card.req_dice[key] = key
        # Die values with no possible placement go to the player's yard
        elif len(placement_dict[key]) == 0:
            # Die must go in a list to go to the yard
            bury_dice.append(key)
    
    # Prompt player for dice placement
    print(f"{prompt_list}\nThese dice values have more than one spot they can"\
        f" be placed.")
    for die in prompt_list:
        while True:
            print(f"Your card options are:\t{placement_dict[die]}")
            # TODO Need to figure out how Card class obj printing will work and 
            # how to translate player input to card obj name for the next step
            selection = input(f"Of the cards above which one would you like to"\
                f" place the {die} on?\t")
            # TODO Validate input (unsure yet how )
            if selection not in placement_dict[die]:
                print(f"{selection} is not one of the available cards listed above")
                continue
            else:
                break
            
    # Add bury_list to the player's yard
    for die in bury_dice:
        player.yard.append(die)
        
    # Check if the player has busted
    bust(player)
                
        