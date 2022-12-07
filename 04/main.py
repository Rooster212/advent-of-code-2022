# Input: 2 numbers separated by a hyphen
# Example: 2-3
def get_upper_lower_as_numbers(input):
  split_numbers = str(input).split('-')
  return (int(split_numbers[0]), int(split_numbers[1]))

def line_does_fully_overlap(input_line):
  input_line = str(input_line).split(',')
  first_lower, first_upper = get_upper_lower_as_numbers(input_line[0])
  second_lower, second_upper = get_upper_lower_as_numbers(input_line[1])

  # If first numbers overlap fully the second numbers
  if(first_lower <= second_lower and first_upper >= second_upper):
    return True
  # If second numbers overlap fully the first numbers
  elif(second_lower <= first_lower and second_upper >= first_upper):
    return True

  return False

def line_does_overlap(input_line):
  input_line = str(input_line).split(',')
  first_lower, first_upper = get_upper_lower_as_numbers(input_line[0])
  second_lower, second_upper = get_upper_lower_as_numbers(input_line[1])

  if(first_lower <= second_lower and second_lower <= first_upper):
    return True
  elif(first_lower <= second_upper and second_lower <= first_upper):
    return True
  elif(second_lower <= first_lower and first_lower <= second_upper):
    return True
  elif(second_upper <= first_upper and first_upper <= second_upper):
    return True

  return False


def main():
  with open("input.txt") as f:
    fully_contained_count = 0
    partially_contained_count = 0

    for line in f:
      if not line.strip():
        break
      else:
        # part 1
        result = line_does_fully_overlap(line)
        if(result == True):
          fully_contained_count += 1

        # part 2
        result = line_does_overlap(line)
        if(result == True):
          partially_contained_count+= 1

    print("Fully contained count: " + str(fully_contained_count))
    print("Partially contained count: " + str(partially_contained_count))

if __name__ == '__main__':
  main()