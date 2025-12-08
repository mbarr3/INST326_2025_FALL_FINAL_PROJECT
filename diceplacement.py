import bust
def dice_placement(player, dice_list):
    """
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

        Sets the attributes name, req_dice, and fulfilled_dice
        
    Returns:
    
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
        while True:
            card_choice = input(f"\nEnter the name of the card you would like to "\
                f"place the {die} on (if you have no place to put the die, enter"\
                    f" the word yard): ")
            if card_choice == 'yard':
                player.yard.append(die)
                bust(player)
                break
            else:
                for card in player.active_cards:
                    if card.name == card_choice:
                        card.req_dice[die] == True

    
    
    # placement_dict = {}
    # prompt_list = []
    # bury_dice = []
    # for die in dice_list:
    #     placement_dict[die] = []
    # for key in placement_dict.keys():
    #     for card in player.active_cards:
    #         for die in card.req_dice.keys():
    #             if card.req_dice[key] == False:
    #                 placement_dict[key].append(card)
    
    # # Place die automatically on a card or in the yard OR prompt player to choose placement if multiple options   
    # for key in placement_dict.keys():
    #     # Place any values with multiple placement options in a list
    #     if len(placement_dict[key]) > 1:
    #         prompt_list.append(key)
    #     # Automatically place die values on a card if only one placement is available
    #     elif len(placement_dict[key]) == 1:
    #         open_card = placement_dict[key]
    #         open_card.req_dice[key] = key
    #     # Die values with no possible placement go to the player's yard
    #     elif len(placement_dict[key]) == 0:
    #         # Die must go in a list to go to the yard
    #         bury_dice.append(key)
    
    # # Prompt player for dice placement
    # print(f"{prompt_list}\nThese dice values have more than one spot they can"\
    #     f" be placed.")
    # for die in prompt_list:
    #     while True:
    #         print(f"\nYour card options are:\n")
    #         counter = 1
    #         for card in placement_dict[die]:
    #             print(f"{counter}. {card}")
    #             counter+=1
    #         # TODO Need to figure out how Card class obj printing will work and 
    #         # how to translate player input to card obj name for the next step
    #         selection = input(f"\n\nEnter the name of the card above which "\
    #             f"one would you like to place the {die} on?\t")
    #         # TODO Validate input
    #         # Mark die spot on the chosen card as fulfilled
    #         for card in placement_dict[die]:
    #             if card.name == (selection):
    #                 card.req_dice[die] = True
                        
    # Add bury_list to the player's yard
    #for die in bury_dice:
       # player.yard.append(die)

                
        