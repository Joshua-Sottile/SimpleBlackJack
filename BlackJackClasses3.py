import random

suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
rank_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
              'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
dict_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
               'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
               'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = dict_values[rank]

    def __str__(self):
        return (f'{self.rank} of {self.suit}')


class Deck:
    def __init__(self):
        self.full_deck = []
        for suit in suits:
            for rank in rank_names:
                created_card = Card(suit, rank)
                self.full_deck.append(created_card)

    def shuffle_up(self):
        random.shuffle(self.full_deck)

    def hit_me(self):
        return self.full_deck.pop(0)


class Dealer:
    def __init__(self):
        self.hand = []

    def add_card(self, new_card):
        self.hand.append(new_card)

    def flip_cards(self):
        print(self.hand[0])
        print('HIDDEN CARD')

    def reveal(self):
        for c in self.hand:
            print(c)


class Player:
    def __init__(self, bank):
        self.hand = []
        self.bank = bank

    def add_card(self, new_card):
        self.hand.append(new_card)

    def flip_cards(self):
        for c in self.hand:
            print(c)

    def place_bet(self, amount):
        self.bank = self.bank - amount
        return amount