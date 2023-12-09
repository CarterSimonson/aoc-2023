def read_input():
  with open('challenges/day_one/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

puzzle_input = read_input()

# puzzle_input = [
#   '1abc2',
#   'pqr3stu8vwx',
#   'a1b2c3d4e5f',
#   'treb7uchet'
# ]

def parse_value(input):
  # search for the first digit (start to end)
  start_digit = ""

  for char in input:
    if char.isdigit():
      start_digit = char
      break

  # search for the second digit (end to start)
  end_digit = ""
  for char in reversed(input):
    if char.isdigit():
      end_digit = char
      break

  # combine digits
  return int(start_digit + end_digit)

puzzle_values = [parse_value(x) for x in puzzle_input]
answer = sum(puzzle_values)

print("The answer is " + str(answer))