import re
import math

def read_input():
  with open('challenges/day_three/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

engine_schematic = read_input()
part_numbers = []

def extract_part_numbers(y):
  line = engine_schematic[y]
  iterator = re.finditer(r'(\d+)', line)

  for match in iterator:
    span = match.span()
    
    part_numbers.append({
      'part': int(match.group()),
      'y': y,
      'start_x': span[0],
      'end_x': span[1] - 1
    })

for y in range(len(engine_schematic)):
  extract_part_numbers(y)

# (x, y): [part_number_a, part_number_b]
gear_adjacency = {}

def add_gear_part(x, y, part):
  gear_pos = (x, y)
  gear = gear_adjacency.get(gear_pos, None)
  
  if (gear):
    gear_adjacency[gear_pos].append(part)
  else:
    gear_adjacency[gear_pos] = [part]

def find_adjacent_gears(part_number):
    part = part_number['part']
    y = part_number['y']
    start_x = part_number['start_x']
    end_x = part_number['end_x']
    
    # Search from 1 place before/above the start to 1 place after the end/below
    x_range = range(start_x - 1, end_x + 2)
    y_range = range(y - 1, y + 2)
    
    for y in y_range:
      if y < 0 or y > len(engine_schematic) - 1:
        continue
      line = engine_schematic[y]
      
      for x in x_range:
        if x < 0 or x > len(line) - 1:
          continue
        char = line[x]
        if char != '*':
          continue
        
        # We found a gear! Add this part to its adjacency list
        add_gear_part(x, y, part)

for part_number in part_numbers:
  find_adjacent_gears(part_number)

def calculate_gear_ratio(part_numbers):
  # Gears must be adjacent to at least two part numbers
  if len(part_numbers) < 2:
    return 0
  
  return math.prod(part_numbers)

gear_ratios = list(map(calculate_gear_ratio, gear_adjacency.values()))
answer = sum(gear_ratios)

print('Answer ' + str(answer))