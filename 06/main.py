def get_marker_part_1(input: str):
    return get_location_in_string(input, 4)


def get_marker_part_2(input: str):
    return get_location_in_string(input, 14)


def get_location_in_string(input: str, desired_marker_length: int):
    for i in range(len(input)):
        characters = input[i:i+desired_marker_length]
        if len(set(characters)) == desired_marker_length:
            return i+desired_marker_length


def main():
    with open("input.txt") as f:
        input = f.read().removesuffix('\n')
        print("Start of packet marker - end index | " +
              str(get_marker_part_1(input)))
        print("Start of message marker - end index | " +
              str(get_marker_part_2(input)))


if __name__ == '__main__':
    main()
