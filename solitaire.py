import random


card_values = list(range(1,14))
suits = ["clubs", "diamonds", "hearts", "spades"]
 
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
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards


cards = generate_cards()
# uncomment this to see the values in the deck of cards
# for card in cards:
#     print(card.value, card.suit)


#variables for the game
num_piles = 7
cards_in_pile = (num_piles*(num_piles-1))/2
cards_in_stock = 52-cards_in_pile
max_pile_size = 20

def initialize_game(deck):
    game_board = []
    for i in range(1,num_piles+1):
        arr = []
        for j in range(i):
            random_card = random.choice(deck)
            arr.append(random_card)
            deck.pop(deck.index(random_card))
        game_board.append(arr)
    return game_board

game_board = initialize_game(cards)

# def print_game_board(game_board):
#     for i in range(len(game_board)):
#         for j in range(len(game_board[i])):
#             print(game_board[i][j].value, game_board[i][j].suit, end=" ")
#         print()

# print_game_board(game_board)

random.shuffle(cards)

# for i in range(len(cards)):
#     print(cards[i].value, cards[i].suit, end=" ")

fundamental_deck = [['Spades',0],['Hearts',0],['Clubs',0],['Diamonds',0]]

def show_game_board(game_board):
    for i in range(len(fundamental_deck)):
        print(f'{fundamental_deck[i][0]} : {fundamental_deck[i][1]}')
    for i in range(len(game_board)):
        print(f'[{game_board[i][0].value},{game_board[i][0].suit}]', end=" ")

show_game_board(game_board)