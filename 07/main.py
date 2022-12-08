class Day07:
    def __init__(self):
        self.pwd_location = []

    def get_pwd_location(self):
        return self.pwd_location

    def process_line(self, line: str):
        # Command
        if line.startswith('$'):
            command = line.removeprefix("$ ")
            print("Running command '" + command + "'")
        else:
            print(line)

    def process_command(self, command: str):
        if command.startswith('cd '):
            folder = command.removeprefix("cd ")
            if folder == "/":
                self.pwd_location = ["/"]
            elif folder == "..":
                self.pwd_location = self.pwd_location[:-1]
            else:
                self.pwd_location.append(folder)


def processor(input_lines):
    current_directory_structure = []
    # First we deal with commands


def main():
    print("main")


if __name__ == "__main__":
    main()
