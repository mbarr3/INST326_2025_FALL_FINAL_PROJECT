import random
from fetch_function import fetch
from gobble_trick import gobble
from Howlfuc import howl
from roll_over import rollover
from trot_trick import trot
from chase_trick import chase
from diceplacement import dice_placement
from trick_tracker import active_tricks, inactive_tricks, display_tricks, select_trick, use_trick, refresh_tricks
from player_card import Player, Card            

total_rolls = [] 

def game_setup():
    """Initial set up for the game, establishing number and names of players,
    and turn order
    
    Side effects: 
        Creates Player class objects
        Creates player list to store player class objects
        Sorts the player_list in descending order by player.yard value
    Returns:
        player_list (list of player obj)
        
    Author: Mackenzie Barrett
    Technique: Key function
    """
    player_list = []
    # Prompt how many players (1-4)
    while True:
        player_count = int(input("\nWelcome to Spots! How many players want to play the "\
            "game? (1-4): "))
        # Validate input
        if not isinstance(player_count, int) or player_count not in range(1,5):
            print(f"{player_count} is not a valid option between 1 and 4")
            continue
        # Initiate Player class for each player 
        count = 1
        for player in range(1, (player_count+1)):
            name = input(f"Player {count} please enter your name: ")
            player_list.append(Player(name))
            count+=1
        break   
           
    # Determine first player by the player with the highest buried die
        # Each player gets a die rolled and buried in their yard when instantiated
        # For the sake of the program establish turn order based on descending buried dice amounts
    player_list.sort(reverse = True, key = lambda x : x.yard)
    
    return player_list


# turn loop
def turn(player_list):
    """Main game loop that handles player turns
    
    Args:
        player_list (list): List of Player objects in turn order
    Side effects:
        Establishes active_tricks (list), dead_tricks (list), and trick 
            descriptions (dict) to track tricks and prompt player actions
        Establishes completable cards list and fulfilled count variable to track 
            cards players can complete
        Modifies player attributes, prints to console, manages game state
        
    Returns:
        None (exits when a player wins)
        
    Author: Noah Aurdos,
    """
    
    active_tricks = ['chase', 'fetch', 'gobble', 'howl', 'roll over', 'trot']
    
    dead_tricks = []
    
    trick_descriptions = {
    'chase': "Roll 1 die. You may repeat this trick as many times as you want but each time roll 1 more die than you just did (2, 3, 4...)", 
    'fetch': "Roll 8 dice. Choose a number you rolled, and place or bury all dice of that number.Discard the rest.", 
    'gobble': "Take 7 treats. Then return 1 treat for each spot in your highest unfilled space.", 
    'howl': "If you have fewer than 6 dog cards, draw the top card of the dog deck and add it to your pack. Then roll 1 die.", 
    'roll over': "Roll all your buried dice and then place or rebury them. Then you may roll 2 dice.", 
    'trot': "You may move 1 die on your dog cards to any other space, changing the number if needed. Then roll 2 dice."
    }

    while True:
        for player in player_list:
            print(f"\n--- {player.name}'s Turn ---")
            print(f"Treats: {player.treats}")
            print(f"Yard: {sum(player.yard)}\n")
            print("Your active dog cards are:\n")
            for card in player.active_cards:
                print(f"{card}\n")
            
            
            # Check if player has a card that CAN be completed
            completable_cards = []
            for card in player.active_cards:
                if Card.check_completion(card):
                    completable_cards.append(card)
                    
            
            if len(completable_cards) > 0:
                response = input(f"\nYou have {len(completable_cards)} card(s)"\
                    f"that can be completed. Complete them now? (yes/no): ")
                if response.lower() in ['yes', 'y']:
                    for card in completable_cards:
                        player.completed_cards.append(card)
                        player.active_cards.remove(card)
                        print(f"Completed card: {card.name}")
                        # Deal a card to replace the completed card
                        player.active_cards.append(Card())
                    print("Your updated active dog cards are:\n")
                    for card in player.active_cards:
                        print(f"{card}\n")
                    continue
                    
            
            # Display available tricks
            print("\n" + "="*50)
            for i in range(len(active_tricks)):
                trick = active_tricks[i]
                print(f"{i+1}. {trick.capitalize()}: {trick_descriptions[trick]}")
                print("="*50)        

            # Prompt player to select their turn action
            while True:
                trick = (input(f"\nWhat action would you like to take this turn: ").lower())
                # Move trick from active tricks list to dead_tricks list
                if trick in active_tricks:
                     idx = active_tricks.index(trick) 
                     dead_tricks.append(active_tricks[idx])
                     active_tricks.remove(trick)

                     break
                else:
                    print("Invalid selection, select an ACTIVE TRICK!")
                    
            # TODO TESTING
            print(active_tricks)
            print(dead_tricks)
            
            # Call the trick function and deactivate it
                # Execute trick based on which one was chosen
            if trick == ('chase'):
                bust_test = chase(player, total_rolls)
            
            elif trick == ('fetch'):
                bust_test = fetch(player, total_rolls)
                
            elif trick == ('gobble'):
                bust_test = gobble(player)
                
            elif trick == ('howl'):
                bust_test = howl(player, total_rolls)
                
            elif trick == ('roll over'):
                bust_test = rollover(player, total_rolls)
                
            elif trick == ('trot'):
                bust_test = trot(player, total_rolls)
                
            # Determine if player turn should continue
            if bust_test == True:
                continue
                
            # Check if all tricks used, refresh if needed
            if len(active_tricks) == 1:
                active_tricks.extend(dead_tricks)
                dead_tricks.clear()
                print("\nAll tricks refreshed!")
            
            # Check if all the player's dog cards are completed
            fulfilled_count = 0
            for card in player.active_cards:
                if card.check_completion():
                    fulfilled_count += 1
                    
            if fulfilled_count == len(player.active_cards) and len(player.active_cards) > 0:
                # If all of a player's dog cards are filled in one turn
                # they are automatically completed and locked
                for card in player.active_cards[:]:
                    player.completed_cards.append(card)
                    player.active_cards.remove(card)
                print("\nCongrats! You fulfilled all your dog cards this turn!")
                print("Your dog cards have been automatically marked as completed!")
    
        # Score check at the end of every round to see if any player won
        for player in player_list:
            if len(player.completed_cards) == 6:
                print(f"\n{'='*50}")
                print(f"GAME OVER! {player.name} wins with 6 completed cards!")
                print(f"{'='*50}")
                
                
def main():
    player_list = game_setup()
    turn(player_list)

if __name__ == "__main__":
    main()

