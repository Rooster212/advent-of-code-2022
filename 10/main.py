import pprint


def run_commands(commands, cycle_limit=1000):
    cycle_counter = 1
    x_register = 1
    history = {}

    current_instruction = None
    current_instruction_end = 0

    while cycle_counter < cycle_limit:
        # Start of cycle - begin instruction
        command = None
        if current_instruction == None:
            if len(commands) > 0:
                command = commands.pop(0)
            else:
                command = None

        if command and command.startswith("addx"):
            current_instruction = "addx"
            current_instruction_arg = int(command.split(' ')[1])
            current_instruction_end = cycle_counter + 2

        history[cycle_counter] = {
            "clock": cycle_counter,
            "x": x_register,
            "signal_strength": x_register * cycle_counter
        }

        # End instruction
        cycle_counter += 1

        # After instruction
        if current_instruction != None and current_instruction_end == cycle_counter:
            if current_instruction == "addx":
                x_register += current_instruction_arg
            current_instruction = None
            current_instruction_arg = 0
            current_instruction_end = 0

    return history


def main():
    with open("input.txt") as f:
        commands = f.read().splitlines()
        result = run_commands(commands)

        target_signal_strengths = [20, 60, 100, 140, 180, 220]

        sum_signal_strength = 0
        for t in target_signal_strengths:
            sum_signal_strength += result[t]['signal_strength']

        print(sum_signal_strength)


if __name__ == "__main__":
    main()
