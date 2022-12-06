import functools

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors


def calculate(opponent, personal):
  result = win_mappings[str(opponent)+str(personal)]
  selected_score = score_mappings[personal]
  result_score = outcome_mappings[result]

  overall_score = selected_score + result_score
  return (result, overall_score)

win_mappings = {
 "AX": "draw",
 "AY": "win",
 "AZ": "lose",
 "BX": "lose",
 "BY": "draw",
 "BZ": "win",
 "CX": "win",
 "CY": "lose",
 "CZ": "draw",
}

score_mappings = {
  'X': 1,
  'Y': 2,
  'Z': 3,
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