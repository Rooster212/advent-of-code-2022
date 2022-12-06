def letter_to_priority(character):
  asciiValue = ord(character)
  if asciiValue > 96:
    return asciiValue - 96
  else:
    return asciiValue - 38

def retrieve_items_from_line(line):
  line_as_array = [char for char in line]
  half_length = len(line_as_array) // 2
  first_half, second_half = line_as_array[:half_length], line_as_array[half_length:]
  return (first_half, second_half)

