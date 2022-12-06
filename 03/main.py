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

def find_common_item(item_sets):
  return set(item_sets[0]).intersection(item_sets[1]).intersection(item_sets[2])

def process(input_file_contents):
  priority_sum = 0

  line_counter = 0
  group_array = []
  group_priority_sum = 0
  for line in input_file_contents:
    if not line.strip():
      break
    else:
      clean_line = str(line).removesuffix('\n')
      items = retrieve_items_from_line(clean_line)
      priority_sum += priorities_for_array(items)

      # Calculate badge
      if line_counter <= 2:
        group_array.append(set(clean_line))

      if line_counter == 2:
        common_item = find_common_item(group_array)
        group_priority_sum += priorities_for_array(common_item)

        # Reset group variables
        line_counter = 0
        group_array = []
      else:
        line_counter += 1


  return priority_sum, group_priority_sum

def main():
  with open("input.txt") as f:
    result = process(f)
    print(result)

if __name__ == '__main__':
  main()