import functools

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors

def calculate(opponent, result):

  item_choice = choice_mappings[str(opponent)+str(result)]
  selected_score = item_choice_mappings[item_choice]
  result_score = outcome_mappings[win_mappings[result]]

  overall_score = selected_score + result_score
  return (result, overall_score)

# AX = Opponent picked Rock. X = Lose so pick Scissors.

choice_mappings = {
 "AX": "C",
 "AY": "A",
 "AZ": "B",
 "BX": "A",
 "BY": "B",
 "BZ": "C",
 "CX": "B",
 "CY": "C",
 "CZ": "A",
}

win_mappings = {
  'X': "lose",
  'Y': "draw",
  'Z': "win",
}

item_choice_mappings = {
  "A": 1,
  "B": 2,
  "C": 3,
}

outcome_mappings = {
  "win": 6,
  "draw": 3,
  "lose": 0,
}

def main():
  total_score = 0

  with open('input.txt') as f:
    for line in f:
      if not line.strip(): # last line
        exit
      else:
        gameline = line.removesuffix('\n').split(' ')
        result, score = calculate(gameline[0], gameline[1])
        total_score += score

    print(total_score)

if __name__ == '__main__':
  main()