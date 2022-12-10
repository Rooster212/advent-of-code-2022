
import unittest
import main

# ..##..
# ...##.
# .####.
# ....#.
# s###..


class Day09Tests(unittest.TestCase):
    test_motions = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]

    def test_get_move_from_line_1(self):
        day_8 = main.Day09()
        result = day_8.get_move_from_line("R 4")
        self.assertEqual(result, ('R', 4))

    def test_get_move_from_line_2(self):
        day_8 = main.Day09()
        result = day_8.get_move_from_line("L 3")
        self.assertEqual(result, ('L', 3))

    def test_get_move_from_line_3(self):
        day_8 = main.Day09()
        result = day_8.get_move_from_line("D 12")
        self.assertEqual(result, ('D', 12))

    def test_calculate_motions_part_1(self):
        day_8 = main.Day09()
        result = day_8.calculate_motions_part_1(self.test_motions)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()
