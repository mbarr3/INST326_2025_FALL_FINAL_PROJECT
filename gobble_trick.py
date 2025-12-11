from random_roll import roll

def gobble(player):
    """Function for the gobble trick card

    Take 7 treats
    THEN
    Return 1 treat for each spot in your highest unfilled space

    Args: 
        player (Player obj): provides Player attributes yard and active_cards 
            which provides Card class obj attributes
    Side effects:
        Establishes treat and blank_max variables to calculate how many treats
            the player receives
    Returns:
        False (bool): False for the sake of the bust test in the turn function

    Author: 
    Technique:
    """
    treat = 7
    blank_max = 0
    for card in player.active_cards:
        for dice in card.req_dice:
            if not card.req_dice[dice]:
                if blank_max < dice:
                    blank_max = dice
    player.treats = player.treats + (treat - blank_max)
    print(f"\nYour updated treats amount is {player.treats} treats!")
    
    return False
            