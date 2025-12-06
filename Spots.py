# Create rough outline of the program
import random

class Player:
    """A player in the game that also tracks their current dog cards,treats, 
    and score.
    """
    def __init__(self, name):
        """
        Args:
        Side effects:
        Returns:
        """
        self.name = name
        # List of Card class objects
        self.active_cards = []
        self.completed_cards = []
        self.total_cards = ((len(self.active_cards)) + (len(self.completed_cards)))
        self.treats = 1
        self.yard = random.randint(1,6)
        # Deal initial 2 cards to the player
        for card in range(2):
            self.cards.append(Card())
    
class Card:
    """Represents a dog card including the card's name and dice requirements
    """
    def __init__(self):
        """
        Args:
        Side effects:
        Returns:
        """
        used_names = []
        while True:
            # List of names for dog cards
            card_names = ["Max", "Luna", "Bella", "Gus", "Teddy", "Daisy", "Bear",
                        "Willow", "Finn", "Molly", "Cooper", "Nala", "Rocky", 
                        "Coco", "Milo", "Cookie", "Buster", "Roxy", "Rex", "Jack",
                        "Archie", "Missy", "Lottie", "Poppy", "Honey", "Lady", 
                        "Ollie", "Diesel", "Duke", "Sadie"]
            random_name = random.choice(card_names)
            if random_name in used_names:
                continue
            else:
                self.name = random_name
                used_names.append(self.name)
                break
        # Assign a random number of dice between 1 and 4 to the card and then
        # assign random values between 1 and 6 to each die
        dice_num = random.randint(1,4)
        req_dice = set()
        fulfilled_dice = set()
        for die in range(1,dice_num+1):
            req_dice.add(random.randint(1,6))


def game_setup():
    """
    Args:
    Side effects:
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
            player_list.append([Player(name), name.yard])            
        # Determine first player by the player with the highest buried die
            # Each player gets a die rolled and buried in their yard when instantiated
            # For the sake of the program establish turn order based on descending buried dice amounts
        player_list.sort(reverse = True, key = lambda player: player[1])
        
active_tricks = ['Chase', ]
# turn loop
def turn():
    
    # prompt player to pick a trick card
        # call the trick function (# deactivate function until it is refreshed)
            # allow the player to place dice if necessary
            # prompt player to spend a treat if applicable (maybe all 
                # functions that involve rolling are while loops and at the 
                # end players are prompted to spend a treat and this decides
                # if the while loop restarts or breaks
                # check the players yard to see if they bust
                    # call the bust function if necessary
                # check if all the players dog cards are completed 
                    # (if all of a players dog cards are filled in one turn
                    # they are automatically completed and locked)
        
        # Score check at the end of every player turn to check if any player
            # has completed the required 6 dog cards to win