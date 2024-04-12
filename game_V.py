import deck_V
import random

class game:

    def __init__(self):
        self.deck = deck_V.generate_deck()
        self.foundation = []
        self.piles = []
        for i in range(4):
            self.foundation.append(deck_V.foundation())
        for i in range(deck_V.num_piles): 
            self.piles.append(deck_V.pile())

    def initialize(self):
        for i in range(deck_V.num_piles):
            for j in range(i+1):
                random_card = random.choice(self.deck)
                self.piles[i].cards.append(random_card)
                self.piles[i].face_card += 1
                self.deck.pop(self.deck.index(random_card))
        random.shuffle(self.deck)
    
    def move_turn_stock(self):
        if len(self.deck)==0:
            return False
        else:
            self.deck.append(self.deck[0])
            self.deck.pop(0)

    def move_stack_to_foundation(self):
        ele = self.deck[0]
        for i in deck_V.suits:
            if i == ele.suit:
                self.found_ind = deck_V.suits.index(i)
        if ele.rank == 1:
            self.foundation[self.found_ind].current_card = ele
            self.foundation[self.found_ind].cards += 1
            self.deck[0] = self.deck[len(self.deck)-1]
            self.deck.pop(len(self.deck)-1)
            return True
        elif self.foundation[self.found_ind].cards != 0 and self.foundation[self.found_ind].current_card.rank == ele.rank-1:
            self.foundation[self.found_ind].current_card = ele
            self.foundation[self.found_ind].cards += 1
            self.deck[0] = self.deck[len(self.deck)-1]
            self.deck.pop(len(self.deck)-1)
            return True
        else:
            return False
        
    def move_stack_to_pile(self,index):
        index -= 1
        if self.piles[index].face_card == -1:
            if(self.deck[0].rank == 11):
                self.piles[index].cards.append(self.deck[0])
                self.deck[0] = self.deck[len(self.deck)-1]
                self.deck.pop(len(self.deck)-1)  
                return True
            else:
                return False
        else:
            if(self.deck[0].rank == self.piles[index].cards[-1].rank-1):
                print("entered")
                if(self.deck[0].suit in deck_V.black_suit and self.piles[index].cards[-1].suit not in deck_V.black_suit):
                    self.piles[index].cards.append(self.deck[0])
                    self.deck[0] = self.deck[len(self.deck)-1]
                    self.deck.pop(len(self.deck)-1)
                    return True
                elif(self.deck[0].suit in deck_V.red_suit and self.piles[index].cards[-1].suit not in deck_V.red_suit):
                    self.piles[index].cards.append(self.deck[0])
                    self.deck[0] = self.deck[len(self.deck)-1]
                    self.deck.pop(len(self.deck)-1)
                    return True
                else:
                    return False
            else:
                return False

    def move_pile_to_pile(self,from_,num_ele,to_):
        from_ -= 1
        to_ -= 1
        if (len(self.piles[from_].cards)) == 0:
            return False
        elif(len(self.piles[from_].cards)-num_ele < self.piles[from_].face_card):
            return False
        else:
            from_ele = self.piles[from_].cards[len(self.piles[from_].cards)-num_ele]
            to_ele = self.piles[to_].cards[-1]
            if (self.piles[to_].face_card==-1):
                if(from_ele.rank == 11):
                    self.piles[to_].cards.extend(self.piles[from_].cards[len(self.piles[from_].cards)-num_ele-1:])
                    self.piles[from_].cards = self.piles[from_].cards[:len(self.piles[from_]) - num_ele -1]
                    if(len(self.piles[from_].cards)-num_ele-1< self.piles[from_].face_card):
                        self.piles[from_].face_card -= 1
                    return True
                else:
                    return False
            else:
                if(from_ele.rank == to_ele.rank-1):
                    if from_ele.suit in deck_V.black_suit and to_ele.suit in deck_V.red_suit:
                        self.piles[to_].cards.extend(self.piles[from_].cards[len(self.piles[from_].cards)-num_ele:])
                        self.piles[from_].cards = self.piles[from_].cards[:len(self.piles[from_].cards) - num_ele]
                        if(len(self.piles[from_].cards)-num_ele< self.piles[from_].face_card):
                            self.piles[from_].face_card -= 1
                        return True
                    elif from_ele.suit in deck_V.red_suit and to_ele.suit in deck_V.black_suit:
                        self.piles[to_].cards.extend(self.piles[from_].cards[len(self.piles[from_].cards)-num_ele :])
                        self.piles[from_].cards = self.piles[from_].cards[:len(self.piles[from_].cards) - num_ele ]
                        if(len(self.piles[from_].cards)-num_ele< self.piles[from_].face_card):
                            self.piles[from_].face_card -= 1
                        return True
                    else:
                        return False

    def move_pile_to_foundation(self,from_):
        from_ -= 1
        ele = self.piles[from_].cards[len(self.piles[from_].cards)-1]
        for i in deck_V.suits:
            if i == ele.suit:
                self.found_ind = deck_V.suits.index(i)
        if(self.piles[from_].face_card != -1):
            if ele.rank == 1:
                self.foundation[self.found_ind].current_card = ele
                self.foundation[self.found_ind].cards += 1
                if(from_ == self.piles[from_].face_card):
                    self.piles[from_].cards.pop()
                    self.piles[from_].face_card -= 1
                else:
                    self.piles[from_].cards.pop()
                return True
            elif self.foundation.current_card.rank == ele.rank-1:
                self.foundation[self.found_ind].current_card = ele
                self.foundation[self.found_ind].cards += 1
                if(from_ == self.piles[from_].face_card):
                    self.piles[from_].cards.pop()
                    self.piles[from_].face_card -= 1
                else:
                    self.piles[from_].cards.pop()
                return True
            else:
                return False
        else:
            return False
        
    #make display functions available
    def display(self):
        print("\n"*5)
        print(f'current stock card: {self.deck[0].value} {self.deck[0].suit}')
        print("Foundation decks are:")
        for i in range(4):
            if(self.foundation[i].current_card == 0):
                print(f'{deck_V.suits[i]} : {self.foundation[0].current_card}' )
            else:
                print(f'{deck_V.suits[i]} : {self.foundation[i].current_card.value} {self.foundation[i].current_card.suit}')
        print("pile : ")
        for i in range(deck_V.num_piles):
            print(f'Pile {i+1} : ' , end='')
            for k in range(self.piles[i].face_card):
                print("*****" , end=" ")
            for j in range(self.piles[i].face_card,len(self.piles[i].cards)):
                if(self.piles[i].cards == []):
                    pass
                else:
                    print(f'[{self.piles[i].cards[j].value} {self.piles[i].cards[j].suit}]', end=" ")
            print()

    def game_score(self):
        self.score = 0
        for i in range(4):
            self.score += ((self.foundation[i].cards)*(self.foundation[i].cards+1))/2
        return  self.score

    def display_legal_moves(self):
        print("""
              1. Press 0 to exit
              2. Press 1 to show this help menu
              3. press 2 to turn the stock
              4. to move from stack to fundamental pile press 3
              5. to move from pile 1 to pile 2 follow 1,[1 - from pile],[number of elements from the end],[2 - to pile]
              6. to move from stack to pile follow 2,[pile number]
              7. to move from pile to fundamental pile follow 3,[pile number]
              """)