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

def init_card_quantity(card: int):
  if (card not in card_quantities):
    card_quantities[card] = 1

def win_cards(current_card: int, wins: int):
  card_quantity = card_quantities[current_card]
  
  # for each win, add the quantity to the following x cards
  for card in range(current_card + 1, current_card + wins + 1):
    init_card_quantity(card)
    card_quantities[card] += card_quantity

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

def check_card(card):
  card_number = parse_numbers(card)[0]
  winning_numbers = parse_winning_numbers(card.split(':')[1])
  card_numbers = parse_card_numbers(card.split(':')[1])
  
  init_card_quantity(card_number)
  
  # Score the card
  wins = len([n for n in card_numbers if n in winning_numbers])
  
  win_cards(card_number, wins)

for card in cards:
  check_card(card)

total = sum(card_quantities.values())

print('Answer: ' + str(total))