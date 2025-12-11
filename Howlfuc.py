from random_roll import roll
from diceplacement import dice_placement
from player_card import Card

def howl(player):
    """Function for the Howl trick
        If player has less than 6 cards call the deal function which will add 
        another card to the player's dog cards. Then the player will roll one die.
    
    Arguments:
        Player class object
    Side-effects:
        Establishes a dice variable to save the value of the rolled die
        Calls the dice placement function to place the rolled die
    Returns:
        bust_test (bool): True/False returned by bust function in dice placement
        
    Author:
    """
    if len(player.active_cards) < 6:
        player.active_cards.append(Card())
    
    while True:
        dice = roll(1)
        
        reroll = None
        
        # Print dice list to the player
        print(f"Your rolled dice are: {dice}")
        
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
        
        bust_test = dice_placement(player, dice)
        if bust_test == True:
            return bust_test