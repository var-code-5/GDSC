import random

#variables for the game
num_piles = 7
cards_in_pile = (num_piles*(num_piles-1))/2
cards_in_stock = 52-cards_in_pile
max_pile_size = 20
fundamental_deck = [['Spades',0],['Hearts',0],['Clubs',0],['Diamonds',0]]
black_suit = ["clubs", "spades"]
red_suit = ["diamonds", "hearts"]


#makes card objects
class Card:
    def __init__(self, value, suit, rank):
        self.value = value
        self.suit = suit
        self.rank = int(rank)

#makes cards
def generate_cards():
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
    cards = []
    for value in card_values:
        for suit in suits:
            if value in face_cards:
                _card = Card(face_cards[value], suit,value)
            else:
                _card = Card(value, suit, value)
            cards.append(_card)
    return cards

#makes the inital configuration of the game
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

#shows the currently available cards in stock
def show_stock(deck):
    print()
    print("Stock : ")
    print(f'[{deck[2].value},{deck[2].suit}]')
    print(f'[{deck[1].value},{deck[1].suit}]')
    print(f'[{deck[0].value},{deck[0].suit}]')

#displays the intial configuration of the game
def show_game_board(game_board,cards):
    for i in range(len(fundamental_deck)):
        print(f'{fundamental_deck[i][0]} : {fundamental_deck[i][1]}')
    for i in range(len(game_board)):
        print(f'pile {i+1} : [{game_board[i][0].value},{game_board[i][0].suit}]')
    show_stock(cards)

# object for the moves of the game
class game_moves():
    #moving form pile to pile
    def move_card_pile(self,play_deck,game_board,from_,to_):
        from_ -= 1
        to_ -= 1
        if(play_deck[from_][0].rank == (play_deck[to_][0].rank)-1):
            if(play_deck[from_][0].suit in black_suit) and (play_deck[to_][0].suit not in black_suit):
                play_deck[to_].append(play_deck[from_][0])
                play_deck[from_].pop(0)
                if(len(play_deck[from_])==0):
                    if(len(game_board[from_]) != 1 or len(game_board[from_]) != 0):
                        game_board[from_].pop(0)
                        play_deck[from_].append(game_board[from_][0])
            else:
                print("INVALID MOVE")
            if(play_deck[from_][0].suit in red_suit) and (play_deck[to_][0].suit not in red_suit):
                play_deck[to_].append(play_deck[from_][0])
                play_deck[from_].pop(0)
                if(len(play_deck[from_])==0):
                    if(len(game_board[from_]) != 0):
                        play_deck[from_].append(game_board[from_][0])
                        game_board[from_].pop(0)
            else:
                print("INVALID MOVE")
        else:
            print("INVALID MOVE")
    
    #moving form stock to pile
    def move_card_stock(self,from_,to_):
        pass

def disp(session):
    for i in range(len(session)):
        print("Pile : "+str((i+1)))
        for j in range(i):
            print(f'[{session[i][j].value},{session[i][j].suit}]',end=" ")
        print("")

def main():
    cards = generate_cards()
    game_board = initialize_game(cards)
    show_game_board(game_board,cards)
    play_deck = [[x[0]] for x in game_board]
    random.shuffle(cards)
    game_move = game_moves()
    while True:
        inp = input()
        try:
            inp_list = eval(inp)
        except:
            pass
        if(inp == 'q'or inp == 'Q'):
            break
        elif(inp_list[0] == 1):
            print("inside")
            game_move.move_card_pile(play_deck,game_board,inp_list[1],inp_list[2])
            disp(play_deck)    
    pass

if __name__ == '__main__':
    main()