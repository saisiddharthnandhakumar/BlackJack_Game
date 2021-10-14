import random

user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over = False

def deal_card():
  random_card = random.choice(cards)
  return random_card

for i in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw."
  elif computer_score == 0:
    return "You lose."
  elif user_score == 0:
    return "You win!"
  elif user_score > 21:
    return "You lose."
  elif computer_score > 21:
    return "Computer went over 21, You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose."

def calculate_score(cards):
  if sum == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

while not is_game_over:

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"Your cards: {user_cards}, Current score: {user_score}")
  print(f"The computer's first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else:
    user_next_card = input("Type 'y' for another card, or 'n' to stop:")
    if user_next_card == 'y':
      user_cards.append(deal_card())
    else:
      is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))
print(f"The computer's cards are:{computer_cards}, with a score of {computer_score}")
print(f"Your cards are:{user_cards}, with a score of {user_score}")