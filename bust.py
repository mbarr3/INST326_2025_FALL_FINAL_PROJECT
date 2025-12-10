def bust (player): 
    """Function meant calculate a player's yard and clear all uncompleted dog cards 
    and yard when a player busts

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
    Side effects:
        Establishes total variable to calculate total value in a player's yard
    Returns:
        Bool: True if the player has busted; False if they player has not busted

    Author: Sean Tully
    Technique:
    """
    total = 0
    for die in player.yard:
        total+=die
    if total > 7:
        player.yard = list()
        for card in player.active_cards:
            for key in card.req_dice.keys():
                card.req_dice[key] = False
        print("Aw, you busted...Your turn is now over. Your yard and active" \
            " cards have been reset.")
        return True 
    else:
        # If the player did not bust
        return False
   
