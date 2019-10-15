import random

suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = []

for s in suits:
    for v in values:
        deck.append(v + " of " + s)

random.shuffle(deck)

print(deck)