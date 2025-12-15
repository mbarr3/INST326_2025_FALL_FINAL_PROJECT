from random_roll import roll
from diceplacement import dice_placement
from player_card import Card

def howl(player,total_rolls):
    """Function for the Howl trick
    
        If player has less than 6 cards call the deal function which will add 
        another card to the player's dog cards. Then the player will roll one die.
    
    Arguments:
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
        total_rolls (list): list of all dice rolled throughout the game
    Side-effects:
        If applicable appends new card obj to player active cards list attribute
            Prints player obj's card objs __str__ in player active cards list 
                attribute 
        If applicable prints info to player that they were not issues new card obj
        Prints info message to player that they will roll 1 die
        Prints rolled die 
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable
        Adds rolled dice to total_rolls
    Returns:
        bust_test (bool): True or False as returned by the bust function
        
    Author: Samuel Onakoya
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
      
    print("\n***~~~Now you roll one die~~~***")  
    while True:
        dice = roll(1)
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
        
        total_rolls.extend(dice)
        
        bust_test = dice_placement(player, dice)
        return bust_test