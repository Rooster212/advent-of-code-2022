import functools

with open('input.txt') as f:
  elf_calorie_totals = []
  highest_elf_sum = 0
  highest_elf = 0

  current_elf = 0
  current_elf_sum = 0

  for line in f:
    if line.strip():
      current_elf_sum += int(line)
    else:
      if current_elf_sum > highest_elf_sum:
        highest_elf_sum = current_elf_sum
        highest_elf = current_elf
      elf_calorie_totals.append(current_elf_sum)
      current_elf_sum = 0
    current_elf += 1

  elf_calorie_totals.sort()

  # print(elf_calorie_totals)

  top_3_elf_calorie_total = elf_calorie_totals[-3:]
  print(top_3_elf_calorie_total)

  print(functools.reduce(lambda a, b: a+b, top_3_elf_calorie_total))
  print("Fattest elf: " + str(highest_elf))
  print("Fattest elf Calorie count: " + str(highest_elf_sum))