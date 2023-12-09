import re

def read_input():
  with open('challenges/day_four/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

cards = read_input()

# Example input: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# You start with one of each scratch card
# Each match for a given card "wins" one of the following cards (2 matches on #1 wins a #2 and a #3)
# The answer is the total number of scratchcards that you end up with

card_quantities = {}

def parse_numbers(input: str):
  return [int(x) for x in re.findall(r'(\d+)', input)]

def parse_winning_numbers(card_text: str):
  split_text = card_text.split(' | ')[0]
  matches = parse_numbers(split_text)
  
  # Convert to a set for more efficient lookup
  return { match for match in matches}

def parse_card_numbers(card_text: str):
    split_text = card_text.split(' | ')[1]
    return parse_numbers(split_text)

def init_card_quantity(card_id: int):
  if (card_id not in card_quantities):
    card_quantities[card_id] = 1

def win_cards(card_id: int, wins: int):
  card_quantity = card_quantities[card_id]
  
  for card in range(card_id + 1, card_id + wins + 1):
    init_card_quantity(card)
    card_quantities[card] += card_quantity

def check_card(card_text):
  card_id = parse_numbers(card_text)[0]
  winning_numbers = parse_winning_numbers(card.split(':')[1])
  card_numbers = parse_card_numbers(card.split(':')[1])
  
  init_card_quantity(card_id)
  
  # Score the card
  wins = len([n for n in card_numbers if n in winning_numbers])
  
  win_cards(card_id, wins)

for card in cards:
  check_card(card)

total = sum(card_quantities.values())

print('Answer: ' + str(total))