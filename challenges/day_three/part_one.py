import re

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

def calculate_part_adjacency(part_number):
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
        if char.isdigit() or char == '.':
          continue
        # If we make it here than the char is a symbol and we should add the part number
        return part

    # If we make it through the entire perimeter without encountering a symbol, don't add the part number
    return 0

part_values = list(map(calculate_part_adjacency, part_numbers))
answer = sum(part_values)

print('Answer ' + str(answer))