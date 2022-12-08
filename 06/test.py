import unittest
import main


class SimpleTest(unittest.TestCase):
    def test_get_marker_part_1_1(self):
        result = main.get_marker_part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        self.assertEqual(result, 7)

    def test_get_marker_part_1_2(self):
        result = main.get_marker_part_1("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(result, 5)

    def test_get_marker_part_1_3(self):
        result = main.get_marker_part_1("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(result, 6)

    def test_get_marker_part_1_4(self):
        result = main.get_marker_part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(result, 10)

    def test_get_marker_part_1_5(self):
        result = main.get_marker_part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
