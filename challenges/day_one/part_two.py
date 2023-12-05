def read_input():
  with open('challenges/day_one/input.txt', 'r') as file:
    lines = file.readlines()

  # Remove any trailing newlines
  return [line.strip() for line in lines]

puzzle_input = read_input()

# puzzle_input = [
#   'two1nine',
#   'eightwothree',
#   'abcone2threexyz',
#   'xtwone3four',
#   '4nineeightseven2',
#   'zoneight234',
#   '7pqrstsixteen'
# ]

reverse_string = lambda s: s[::-1]

# Create a mapping for assigning the digit strings to values
digit_map = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

# List out the digits we care about searching for (including in reverse form)
digits = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine'
]
reversed_digits = list(map(reverse_string, digits))

def get_digit_substring(value, reversed):
  # Search using reversed digit strings if we're searching "back to front"
  digits_to_search = reversed_digits if reversed else digits

  for digit in digits_to_search:
    if value.startswith(digit):
      # Un-reverse the digit to it's normal form if necessary
      ordered_digit = reverse_string(digit) if reversed else digit
      return digit_map[ordered_digit]
  
  return False

def parse_digit(input, reversed):
  # search for the first digit (start to end)
  parsed_digit = ""

  # reverse the input if we're searching "back to front"
  ordered_input = reverse_string(input) if reversed else input

  for i in range(len(ordered_input)):
    char = ordered_input[i]

    # If the char is a digit, we found our number!
    if char.isdigit():
      parsed_digit = char
      break

    # If the char matches the start of a number's word, search forward from the current char for matches
    sliced_input = ordered_input[i:]
    digit_substring = get_digit_substring(sliced_input, reversed)
  
    if digit_substring:
      parsed_digit = digit_substring
      break

  return parsed_digit

def parse_value(input):
  start_digit = str(parse_digit(input, False))
  end_digit = str(parse_digit(input, True))

  return int(start_digit + end_digit)

puzzle_values = list(map(parse_value, puzzle_input))

print("Answer: " + str(sum(puzzle_values)))