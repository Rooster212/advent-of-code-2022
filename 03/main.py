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
  return list(set(first_half).intersection(second_half))

def priorities_for_array(section_list):
  sum = 0
  for item in section_list:
    sum += letter_to_priority(item)
  return sum

def process(input_file_contents):
  priority_sum = 0
  for line in input_file_contents:
    if not line.strip():
      break
    else:
      items = retrieve_items_from_line(line)
      priority_sum += priorities_for_array(items)
  return priority_sum

def main():
  with open("input.txt") as f:
    result = process(f)
    print(result)

if __name__ == '__main__':
  main()