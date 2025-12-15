def bust (player): 
    """Function meant calculate a player's yard and clear all uncompleted dog cards 
    and yard when a player busts

    Args: 
        player (Player obj): provides Player attributes yard and active_cards 
            which provides Card class obj attributes
    Side effects:
        If the player busted: sets the player.yard attribute to an empty list
            Sets all values to False for every Card obj in player.active_cards
            Prints a message to the terminal
    Returns:
        Bool: True if the player has busted; False if they player has not busted

    Author: Sean Tully
    """
    total = 0
    for die in player.yard:
        total+=die
    if total > 7:
        player.yard = list()
        for card in player.active_cards:
            for key in card.req_dice.keys():
                card.req_dice[key] = False
        print("\nAw, you busted...Your turn is now over. Your yard and active" \
            " cards have been reset.")
        return True 
    else:
        # If the player did not bust
        return False
   
