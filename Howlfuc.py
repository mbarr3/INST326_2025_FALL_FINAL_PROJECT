from random_roll import roll
from diceplacement import dice_placement
from player_card import Card

def howl(player,total_rolls):
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
        
    Author: Samuel Onakoya
    Technique: Conditional Expressions
    """
    total_cards = (len(player.active_cards) + len(player.completed_cards))
    
    if total_cards < 6:
        player.active_cards.append(Card())
        # Print the players updated active dog cards 
        print("Your updated active dog cards are:\n")
        for card in player.active_cards:
            print(f"{card}\n")
    else:
        print("You already have 6 dog cards so you were not dealt a new card.")
        
    while True:
        print("\n***~~~Now you roll one die~~~***")
        dice = roll(1)
        total_rolls.extend(dice)
        
        reroll = None
        
        if player.treats > 0:
            while True:
                # Print dice list to the player
                print(f"\nYour rolled dice are: {dice}")
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
        return bust_test