def get_marker_part_1(input: str):
    input_length = len(input)

    i = 3
    while i < input_length:
        i += 1
        characters = input[i-4:i]
        if (len(set(characters)) == 4):
            return i


with open("input.txt") as f:
    input = f.read().removesuffix('\n')
    print(get_marker_part_1(input))
