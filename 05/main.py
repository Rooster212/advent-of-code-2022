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


def process_stacks_and_steps(stacks, steps):
    for line in steps:
        move_count, from_stack, to_stack = step_parse(line)
        for _i in range(move_count):
            item_to_move = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(item_to_move)
            print_stacks(stacks)
    return stacks


def print_stacks(stacks):
    stack_count = 1
    for stack in stacks:
        print(str(stack_count) + " | " + str(stack))
        stack_count += 1
    print("----------------")


def main():
    stacks = get_challenge_input_stacks()

    print("input stacks")
    print_stacks(stacks)

    with open("input_steps.txt") as f:
        result = process_stacks_and_steps(stacks, f)
        stack_count = 1
        for stack in result:
            top_item = stack[len(stack)-1]
            print(str(stack_count) + " | " + top_item)
            stack_count += 1


if __name__ == '__main__':
    main()
