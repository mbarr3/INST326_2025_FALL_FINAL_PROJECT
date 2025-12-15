import random
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
        """Initialize new Player class object
        
        Args:
            name (str): Player's input name
        Side effects:
            Sets attributes name, active_cards, completed_cards, total_cards,
            treats, and yard.
            Also initiates two Card class objects and appends them to the Player
            object's active_cards list  
        
        Author: Mackenzie Barrett 
        Technique: Composition of two custom classes
        """
        self.name = name
        # List of Card class objects
        self.active_cards = []
        self.completed_cards = []
        self.treats = 1
        self.yard = [random.randint(1,6)]
        # Deal initial 2 cards to the player
        for card in range(2):
            while True:
                dupe = False
                new_card = Card()
                if len(self.active_cards) > 0:
                    for dog in self.active_cards:
                        if new_card.name == dog.name:
                            dupe = True
                    if dupe == True:
                        continue
                    else:
                        self.active_cards.append(new_card)
                        break
                else:
                    self.active_cards.append(new_card)
                    break
            
class Card:
    """Represents a dog card including the card's name and dice requirements
    
    Attributes:
        name (str): name of the dog card
        req_dice (dict): key is a die requirement and the value is a boolean of 
                        if it is fulfilled or not
    """
    def __init__(self):
        """Initialize new Card class object
        
        Side effects:
            Sets the attributes name and req_dice
            Establishes list card_names
        
        Author: Noah Aurdos
        """
        # List of names for dog cards 
        # TODO Find a way to alter the list to avoid duplicate dog names?
        card_names = ["Max", "Luna", "Bella", "Gus", "Teddy", "Daisy", "Bear",
                    "Willow", "Finn", "Molly", "Cooper", "Nala", "Rocky", 
                    "Coco", "Milo", "Cookie", "Buster", "Roxy", "Rex", "Jack",
                    "Archie", "Missy", "Lottie", "Poppy", "Honey", "Lady", 
                    "Ollie", "Diesel", "Duke", "Sadie", "Caesar", "Dougie", 
                    "Comet", "Kaya", "Fitz", "Ginger", "Ranger", "Bailey",
                    "Flash", "Peach", "Ripley", "Tank", "Thumper", "Bumper",
                    "River", "Shadow", "Zeke"]
        
        # TODO NEED TO FIX PLAYER HAVING DOGS WITH SAME NAME
        self.name = random.choice(card_names)
        
        # Assign a random number of dice between 1 and 4 to the card and then
        # assign random values between 1 and 6 to each die
        dice_num = random.randint(1,4)
        self.req_dice = {}
        for die in range(1,dice_num+1):
            self.req_dice[random.randint(1,6)] = False
            
    def check_completion(self):
        """Checks if a player has a fulfilled card that can be completed
        
        Returns:
            bool (True/False): True if a card is fulfilled, False if it is not

        Author: Mackenzie Barrett
        """
        if False not in self.req_dice.values():
            return True
        else:
            return False
    
    def __str__(self):
        """Informal representation of a Card class object
            
        Returns:
            str: string containing the name of the Card obj and its requirements
            
        Author: Sean Tully
        Technique: Magic method
        """
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
        