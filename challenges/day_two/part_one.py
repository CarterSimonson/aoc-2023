import re

def read_input():
  with open('challenges/day_two/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

# puzzle_input = [
#   'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#   'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#   'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#   'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#   'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# ]

puzzle_input = read_input()

max_color_quantity = {
  'red': 12,
  'green': 13,
  'blue': 14
}

# Parse the data on a per-game basis to retrieve the following info:
# - Game ID
# - Game sets
def extract_game_id(game_text):
  return int(re.match(r'Game (\d+)', game_text).group(1))

def parse_game_data(raw_game_text):
  # Split the input into two parts: extracting the "Game X" string and path content
  [game_text, set_text] = raw_game_text.split(': ')
  
  game_id = extract_game_id(game_text)
  sets = set_text.split('; ')
  
  return { 'game_id': game_id, 'sets': sets }

# Iterate through the sets for each given game
# - Extract the count for each given color and compare them to our max values
#   - If every set of the game is proven possible, add the game ID to a rolling sum
def is_set_valid(set_text):
  set_values = re.findall(r'(\d+)\s(blue|red|green)', set_text)
  
  for value in set_values:
    quantity = int(value[0])
    color = value[1]
    surpassed_quantity = max_color_quantity[color] < quantity
    
    if (surpassed_quantity):
      return False
  
  return True

def check_game_value(raw_game_text):
  game_data = parse_game_data(raw_game_text)
  
  for set_text in game_data['sets']:
    if (is_set_valid(set_text) == False):
      return 0
  
  return game_data['game_id']

total = sum([check_game_value(x) for x in puzzle_input])
print('Total: ' + str(total))