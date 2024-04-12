
# constants for the game
num_piles = 7
cards_in_pile = (num_piles*(num_piles-1))/2
cards_in_stock = 52-cards_in_pile
max_pile_size = 20


card_values = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #for better understanding
suits = ["clubs", "diamonds", "hearts", "spades"]
black_suit = ["clubs", "spades"]
red_suit = ["diamonds", "hearts"]

face_cards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 1,
    11: "J",
    12: "Q",
    13: "K",
    1: "A"
}
 
class Card:
    def __init__(self, value, suit,rank):
        self.value = value
        self.suit = suit
        self.rank = rank

def generate_deck():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit,value)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards

class foundation:
    cards = 0
    current_card = 0

class stock:
    cards_left = cards_in_stock
    face_card_ind = 0

class pile:
    cards = []
    face_card = -1