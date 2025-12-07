# Create rough outline of the program
import random,bust,chase_trick,dice_placement,fetch_function,gobble_trick,Howlfuc,random_roll,roll_over,trot_trick
from trick_tracker import active_tricks, inactive_tricks, display_tricks, select_trick, use_trick, refresh_tricks


class Player:
    """A player in the game that also tracks their current dog cards,treats, 
    and score.
    
    Attributes:
        name (str): Name of the player
        active_cards (list of Card class objects): List of Card class objects
                that represent the player's active cards
        completed_cards (list of Card class objects): List of Card class objects
                that represent the player's completed cards
        total_cards (int): Expression that calculates the total number of cards
                the player has (cannot exceed 6)
        treats (int): tracks how many treats the player has
        yard (int): tracks the value in the player's yard for bust purposes
    """
    def __init__(self, name):
        """
        Args:
            name (str): Player's input name
        Side effects:
            Sets attributes name, active_cards, completed_cards, total_cards,
            treats, and yard.
            Also initiates two Card class objects and appends them to the Player
            object's active_cards list
        """
        self.name = name
        # List of Card class objects
        self.active_cards = []
        self.completed_cards = []
        self.total_cards = ((len(self.active_cards)) + (len(self.completed_cards)))
        self.treats = 1
        self.yard = [random.randint(1,6)]
        # Deal initial 2 cards to the player
        for card in range(2):
            self.cards.append(Card())
            
    
class Card:
    """Represents a dog card including the card's name and dice requirements
    
    Attributes:
        name (str): name of the dog card
        req_dice (dict): key is a die requirement and the value is a boolean of 
                        if it is fulfilled or not
    """
    def __init__(self):
        """
        Side effects:
            Sets the attributes name, req_dice, and fulfilled_dice
        Returns:
        """
        # List of names for dog cards 
        card_names = ["Max", "Luna", "Bella", "Gus", "Teddy", "Daisy", "Bear",
                    "Willow", "Finn", "Molly", "Cooper", "Nala", "Rocky", 
                    "Coco", "Milo", "Cookie", "Buster", "Roxy", "Rex", "Jack",
                    "Archie", "Missy", "Lottie", "Poppy", "Honey", "Lady", 
                    "Ollie", "Diesel", "Duke", "Sadie"]
        self.name = random.choice(card_names)
        card_names.remove(self.name)
        
        # Assign a random number of dice between 1 and 4 to the card and then
        # assign random values between 1 and 6 to each die
        dice_num = random.randint(1,4)
        self.req_dice = {}
        for die in range(1,dice_num+1):
            self.req_dice[random.randint(1,6)] = False
            
    def check_completion(self):
        """Checks if a player has a fulfilled card that can be completed"""
        if False not in self.req_dice.values():
            True
        else:
            False
    
    def __str__(self):
        back = []
        handoff = ""
        for key in self.req_dice:
            if self.req_dice [key]:
                back.append(str(key) + "\u2705"+"|")
            else:
                back.append (str(key)+"|")
        for entry in back:
            handoff= handoff+entry
        return f"Card Name: {self.name}\n {handoff}"
        
            
def game_setup():
    """Initial set up for the game, establishing number and names of players,
    and turn order
    Side effects: creates Player class objects
    Returns:
    """
    player_list = []
    # Prompt how many players (1-4)
    while True:
        player_count = input("\nWelcome to Spots! How many players want to play the"\
            "game? (1-4):\t")
        # Validate input
        if not isinstance(player_count, int) or player_count not in range(1,5):
            print(f"{player_count} is not a valid option between 1 and 4")
            continue
        # Initiate Player class for each player 
        for player in range(1, (player_count+1)):
            name = input("Please, enter your name:\t")
            player_list.append([Player(name)])
        break   
           
    # Determine first player by the player with the highest buried die
        # Each player gets a die rolled and buried in their yard when instantiated
        # For the sake of the program establish turn order based on descending buried dice amounts
    player_list.sort(reverse = True)
    
    return player_list

    
        
# Descriptions of the tricks for the players when choosing a trick
# TODO find best way to present the descriptions to the player
trick_descriptions = {'Chase': "Roll 1 die. You may repeat this trick as many times as you want but each time roll 1 more die than you just did (2, 3, 4...)", 
                      'Fetch': "Roll 8 dice.\nChoose a number you rolled, and place or bury all dice of that number.\nDiscard the rest.", 
                      'Gobble': "Take 7 treats.\nThen return 1 treat for each spot in your highest unfilled space.", 
                      'Howl': "If you have fewer than 6 dog cards, draw the top card of the dog deck and add it to your pack.\nThen roll 1 die.", 
                      'Roll Over': "Roll all your buried dice and then place or rebury them.\nThen you may roll 2 die.", 
                      'Trot': "You may move 1 die on your dog cards to any other space, changing the number if needed.\nThen roll 2 dice."
                      }



# turn loop
def turn(player_list):
    
    active_tricks = [['Chase', 'Fetch', 'Gobble', 'Howl', 'Roll Over', 'Trot']]
    
    dead_tricks = []
    
    trick_descriptions = {
    'Chase': "Roll 1 die. You may repeat this trick as many times as you want but each time roll 1 more die than you just did (2, 3, 4...)", 
    'Fetch': "Roll 8 dice. Choose a number you rolled, and place or bury all dice of that number.Discard the rest.", 
    'Gobble': "Take 7 treats. Then return 1 treat for each spot in your highest unfilled space.", 
    'Howl': "If you have fewer than 6 dog cards, draw the top card of the dog deck and add it to your pack.Then roll 1 die.", 
    'Roll Over': "Roll all your buried dice and then place or rebury them. Then you may roll 2 dice.", 
    'Trot': "You may move 1 die on your dog cards to any other space, changing the number if needed. Then roll 2 dice."
}

    """Main game loop that handles player turns
    
    Args:
        player_list (list): List of Player objects in turn order
    Side effects:
        Modifies player attributes, prints to console, manages game state
    Returns:
        None (exits when a player wins)
    """
    while True:
        for player in player_list:
            print(f"\n--- {player.name}'s Turn ---")
            print(f"Treats: {player.treats}")
            print(f"Yard: {player.yard}")
            
            
            # Check if player has a card that CAN be completed
            completable_cards = []
            for card in player.active_cards:
                if Card.check_completion(card):
                    completable_cards.append(card)
                    
            
            if len(completable_cards) > 0:
                response = input(f"\nYou have {len(completable_cards)} card(s) that can be completed. Complete them now? (yes/no): ")
                if response.lower() in ['yes', 'y']:
                    for card in completable_cards:
                        player.completed_cards.append(card)
                        player.active_cards.remove(card)
                        print(f"Completed card: {card.name}")
                    
            
            # Display available tricks
            print("\n" + "="*50)
            for i in range(len(active_tricks)):
                trick = active_tricks[i]
                print(f"{i+1}. {trick}: {trick_descriptions[trick]}")
                print("="*50)        

            # Prompt player to select their turn action
            while True:
                trick = input(f"\nWhat action would you like to take this turn: ")
                if trick in active_tricks:
                     idx = active_tricks.index(trick) 
                     dead_tricks.append(active_tricks[idx])
                     active_tricks.remove(trick)

                     break
                else:
                    print("Invalid selection select an ACTIVE TRICK!")
            
            # Call the trick function and deactivate it
            if trick in active_tricks:
                # Execute trick based on which one was chosen
                if trick == 'Chase':
                    chase_trick(player)
                elif trick == 'Fetch':
                    fetch_function(player)
                elif trick == 'Gobble':
                    gobble_trick(player)
                elif trick == 'Howl':
                    Howlfuc(player)
                elif trick == 'Roll Over':
                    roll_over(player)
                elif trick == 'Trot':
                    trot_trick(player)
                
                # Check if all tricks used, refresh if needed
                if len(active_tricks) == 1:
                    refresh_tricks()
            
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