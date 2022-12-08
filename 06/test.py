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

    def test_get_location_in_string_1(self):
        result = main.get_location_in_string(
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
        self.assertEqual(result, 7)

    def test_get_location_in_string_2(self):
        result = main.get_location_in_string("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
        self.assertEqual(result, 5)

    def test_get_location_in_string_3(self):
        result = main.get_location_in_string("nppdvjthqldpwncqszvftbrmjlhg", 4)
        self.assertEqual(result, 6)

    def test_get_location_in_string_4(self):
        result = main.get_location_in_string(
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4)
        self.assertEqual(result, 10)

    def test_get_location_in_string_5(self):
        result = main.get_location_in_string(
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4)
        self.assertEqual(result, 11)

    def test_get_marker_part_2_1(self):
        result = main.get_marker_part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
        self.assertEqual(result, 19)

    def test_get_marker_part_2_2(self):
        result = main.get_marker_part_2("bvwbjplbgvbhsrlpgdmjqwftvncz")
        self.assertEqual(result, 23)

    def test_get_marker_part_2_3(self):
        result = main.get_marker_part_2("nppdvjthqldpwncqszvftbrmjlhg")
        self.assertEqual(result, 23)

    def test_get_marker_part_2_4(self):
        result = main.get_marker_part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
        self.assertEqual(result, 29)

    def test_get_marker_part_2_5(self):
        result = main.get_marker_part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
        self.assertEqual(result, 26)


if __name__ == '__main__':
    unittest.main()
