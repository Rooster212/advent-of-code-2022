with open('input.txt') as f:
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
      current_elf_sum = 0
    current_elf += 1

  print("Fattest elf: " + str(highest_elf))
  print("Calorie count: " + str(highest_elf_sum))