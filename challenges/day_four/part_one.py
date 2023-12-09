def read_input():
  with open('challenges/day_four/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

cards = read_input()

# Example input: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# - Left side is winning numbers
# - Right side is numbers on a given card

# Score a card by determining how many winning numbers are present on a given card
# - score = 2^(wins - 1)

# The total score is the sum of all card scores

import re

def parse_numbers(input: str):
  return [int(x) for x in re.findall(r'(\d+)', input)]

def parse_winning_numbers(card: str):
  split_text = card.split(' | ')[0]
  matches = parse_numbers(split_text)
  
  # Convert to a set for more efficient lookup
  return { match for match in matches}

def parse_card_numbers(card: str):
    split_text = card.split(' | ')[1]
    return parse_numbers(split_text)

def score_card(card):
  # score the card
  card_data = card.split(':')[1]
  winning_numbers = parse_winning_numbers(card_data)
  card_numbers = parse_card_numbers(card_data)
  
  match_count = len([n for n in card_numbers if n in winning_numbers])
  
  if (match_count == 0):
    return 0
  
  # 1 match = 1, 2 matches = 2, 3 matches = 4, etc...
  return pow(2, match_count-1)

scores = [score_card(card) for card in cards]
final_score = sum(scores)

print('Answer: ' + str(final_score))