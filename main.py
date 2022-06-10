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

while not is_game_over:

    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"your cards: {user_card}, current score : {user_score}")
    print(f"computer cards: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get a another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_card.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)