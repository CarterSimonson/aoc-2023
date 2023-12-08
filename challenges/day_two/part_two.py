# Changes:
# - Our new goal is to determine the fewest number of cubes for each given color that a game would require to be valid
# - We must also calculate the power of a game: the number of red * blue * green cubes
# - Summate all of these powers from each game together

import re
import math

def read_input():
  with open('challenges/day_two/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

puzzle_input = read_input()

# puzzle_input = [
#   'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#   'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#   'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#   'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#   'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# ]

def extract_game_id(game_text):
  return int(re.match(r'Game (\d+)', game_text).group(1))

def parse_game_data(raw_game_text):
  # Split the input into two parts: extracting the "Game X" string and path content
  [game_text, set_text] = raw_game_text.split(': ')
  
  game_id = extract_game_id(game_text)
  sets = set_text.split('; ')
  
  return { 'game_id': game_id, 'sets': sets }

def get_set_data(set_text):
  color_values = re.findall(r'(\d+)\s(blue|red|green)', set_text)
  return color_values

def check_game_value(raw_game_text):
  game_data = parse_game_data(raw_game_text)
  
  max_values = {}
  
  # Set text is formatted like this: "3 blue, 4 red" or "1 red, 2 green, 6 blue"
  for set_text in game_data['sets']:
    color_values = get_set_data(set_text)
    
    # Determine the largest value seen for each color
    for color_data in color_values:
      quantity = int(color_data[0])
      color = color_data[1]
      current_max = max_values.get(color, None)
      
      if (current_max == None or quantity > current_max):
        max_values[color] = quantity
  
  return math.prod(max_values.values())

total = sum(list(map(check_game_value, puzzle_input)))
print('Total: ' + str(total))