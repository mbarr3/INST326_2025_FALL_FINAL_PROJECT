
def dice_placement(player, dice_list):
    """
    Args:
        player (Player class obj): Player class object to provide active_cards
                                    list
        dice_list (list of ints): list of dice values that need to either be 
                                placed automatically or by the player if more
                                than one option is available

    Side effects:
        Sets the attributes name, req_dice, and fulfilled_dice
    Returns:
    
    Author: Mackenzie Barrett
    Technique: Sequence Unpacking
    """
    placement_dict = {}
    prompt_list = []
    bury_dice = []
    for die in dice_list:
        placement_dict[die] = []
    for key in placement_dict.keys():
        for card in player.active_cards:
            for die in card.req_dice.keys():
                if card.req_dice[key] == None:
                    placement_dict[key].append([card.name, str(card.req_dice[key])])
                    
    for key, value in placement_dict.keys():
        if len(placement_dict[key]) > 1:
            prompt_list.append([key, value])
        elif len(placement_dict[key]) == 1:
            # Auto place die with dice_placement
            pass
        elif len(placement_dict[key]) == 0:
            # Die must go in a list to go to the yard
            bury_dice.append(key)
            
            
            
                
        