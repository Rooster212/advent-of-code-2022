def get_challenge_input_stacks():
    stacks = [
        ['V', 'R', 'H', 'B', 'G', 'D', 'W'],
        ['F', 'R', 'C', 'G', 'N', 'J'],
        ['J', 'N', 'D', 'H', 'F', 'S', 'L'],
        ['V', 'S', 'D', 'J'],
        ['V', 'N', 'W', 'Q', 'R', 'D', 'H', 'S'],
        ['M', 'C', 'H', 'G', 'P'],
        ['C', 'H', 'Z', 'L', 'G', 'B', 'J', 'F'],
        ['R', 'J', 'S'],
        ['M', 'V', 'N', 'B', 'R', 'S', 'G', 'L']
    ]

    # We reverse all the stacks so that append() and pop() work as stack operators
    for stack in stacks:
        stack.reverse()

    return stacks


def step_parse(line: str):
    # step line looks like the following:
    # "move 1 from 2 to 1"
    line_parts = line.removesuffix('\n').split(' ')
    return (int(line_parts[1]), int(line_parts[3]), int(line_parts[5]))


def process_stacks_and_steps_part1(stacks, steps):
    for line in steps:
        move_count, from_stack, to_stack = step_parse(line)
        for _i in range(move_count):
            item_to_move = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(item_to_move)
    return stacks


def process_stacks_and_steps_part2(stacks, steps):
    for line in steps:
        move_count, from_stack, to_stack = step_parse(line)

        from_stack_index = from_stack - 1
        to_stack_index = to_stack - 1

        from_index = len(stacks[from_stack_index]) - move_count
        items_to_move = stacks[from_stack_index][from_index:]
        items_to_move.reverse()

        remaining_items_stack_count = len(stacks[from_stack_index])-move_count
        stacks[from_stack_index] = stacks[from_stack_index][:remaining_items_stack_count]

        for item in range(len(items_to_move)):
            stacks[to_stack_index].append(items_to_move.pop())
    return stacks


def print_stacks(stacks):
    stack_count = 1
    for stack in stacks:
        print(str(stack_count) + " | " + str(stack))
        stack_count += 1
    print("----------------")


def print_top_items(stacks):
    stack_count = 1
    top_items_as_input = ""
    for stack in stacks:
        top_item = stack[len(stack)-1]
        top_items_as_input += top_item
        print(str(stack_count) + " | " + top_item)
        stack_count += 1

    print("As input | " + top_items_as_input)


def main():
    stacks = get_challenge_input_stacks().copy()

    with open("input_steps.txt") as f:
        result_part_1 = process_stacks_and_steps_part1(stacks, f)
        # Print part1
        print("--------------------------")
        print("Top items - Part 1")
        print_top_items(result_part_1)

        print("--------------------------")

    with open("input_steps.txt") as f:
        stacks = []
        # Copy needed here to avoid modifying original array
        stacks = get_challenge_input_stacks().copy()
        result_part_2 = process_stacks_and_steps_part2(stacks, f)

        # Print part2
        print("Top items - Part 2")
        print_top_items(result_part_2)
        print("--------------------------")


if __name__ == '__main__':
    main()
