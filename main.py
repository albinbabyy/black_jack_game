import random

"""creating a function fro random card generation"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


"""creating empty list for us and computer to store the card values"""
user_card = []
computer_card = []
for _ in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)