

class Day09:

    def __init__(self):
        self.tail_visited_positions = {
            (0, 0): True
        }
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0

    def calculate_motions_part_1(self, motions):
        # Add direction to coordinates one at a time, moving the head

        for motion_line in motions:

            # Now move the head
            direction, count = self.get_move_from_line(motion_line)
            if direction == 'R':
                iterator = 0
                while iterator < count:
                    if (self.manhattan_distance() > 1):
                        self.move_tail(self.head_x, self.head_y)
                    self.head_x += 1
                    iterator += 1
            elif direction == 'L':
                iterator = 0
                while iterator < count:
                    if (self.manhattan_distance() > 1):
                        self.move_tail(self.head_x, self.head_y)
                    self.head_x -= 1
                    iterator += 1
            elif direction == 'U':
                iterator = 0
                while iterator < count:
                    if (self.manhattan_distance() > 1):
                        self.move_tail(self.head_x, self.head_y)
                    self.head_y += 1
                    iterator += 1
            elif direction == 'D':
                iterator = 0
                while iterator < count:
                    if (self.manhattan_distance() > 1):
                        self.move_tail(self.head_x, self.head_y)
                    self.head_y -= 1
                    iterator += 1
            else:
                print("No direction?")

            print("-------------")
            print(self.tail_visited_positions)

        # self.print_visited()
        return len(self.tail_visited_positions)

    def get_move_from_line(self, line: str):
        move = line.split(' ')
        return (move[0], int(move[1]))

    def move_tail(self, old_head_x, old_head_y):
        # Tail follows one behind (i.e. previous position)
        self.tail_x = old_head_x
        self.tail_y = old_head_y

        # Store each position in visited_positions dict (meaning if we visit again it won't be counted again)
        self.tail_visited_positions[(self.tail_x, self.tail_y)] = True

    def manhattan_distance(self):
        return abs(self.tail_x - self.head_x) + abs(self.tail_y - self.head_y)

    # def print_visited(self):
    #     # Find highest numbers

    #     highest_y = max([y[1] for y in self.tail_visited_positions])
    #     highest_x = max([x[0] for x in self.tail_visited_positions])

    #     counter_x = 0
    #     counter_y = highest_y
    #     while counter_x < highest_x:
    #         counter_x += 1
    #         while counter_y > 0:
    #             counter_y -= 1
    #             if counter_x == 0 and counter_y == 0:
    #                 print("s", end="")
    #                 continue
    #             elif (counter_x, counter_y) in self.tail_visited_positions:
    #                 print("#", end="")
    #                 continue
    #             else:
    #                 print(".", end="")
    #         print("", end='\n')
