def get_challenge_input_stacks():
  stacks = [
    ['V','R','H','B','G','D','W'],
    ['F','R','C','G','N','J'],
    ['J','N','D','H','F','S','L'],
    ['V','S','D','J'],
    ['V','N','W','Q','R','D','H','S'],
    ['M','C','H','G','P'],
    ['C','H','Z','L','G','B','J','F'],
    ['R','J','S'],
    ['M','V','N','B','R','S','G','L']
  ]

  # We reverse all the stacks so that append() and pop() work as stack operators
  for stack in stacks:
    stack.reverse()

  return stacks

def main():
  print(get_challenge_input_stacks())

  # stacks = []
  # stack_count = 3

  # # Initialise stacks
  # for stack_number in range(stack_count):
  #   stacks[stack_number] = []


  # # with open("input.txt") as f:


if __name__ == '__main__':
  main()