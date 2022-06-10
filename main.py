import random

"""creating a function fro random card generation"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


""" To calculate the score of user and computer a function defined"""


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


"""creating empty list for us and computer to store the card values"""


user_card = []
computer_card = []
for _ in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

print(f"your cards: {user_card}, current score : {user_score}")
print(f"computer cards: {computer_card[0]}")