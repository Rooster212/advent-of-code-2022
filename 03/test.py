import unittest
import main


class SimpleTest(unittest.TestCase):

  def test_priority1(self):
    result = main.letter_to_priority('A')
    self.assertEqual(result, 27)
  def test_priority2(self):
    result = main.letter_to_priority('z')
    self.assertEqual(result, 26)
  def test_priority3(self):
    result = main.letter_to_priority('a')
    self.assertEqual(result, 1)
  def test_priority4(self):
    result = main.letter_to_priority('c')
    self.assertEqual(result, 3)

  # examples from day page
  def test_retrieve_items_from_line_1(self):
    result = main.retrieve_items_from_line("vJrwpWtwJgWrhcsFMMfFFhFp")
    self.assertEqual(result, ['p'])
  def test_retrieve_items_from_line_2(self):
    result = main.retrieve_items_from_line("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    self.assertEqual(result, ['L'])
  def test_retrieve_items_from_line_3(self):
    result = main.retrieve_items_from_line("PmmdzqPrVvPwwTWBwg")
    self.assertEqual(result, ['P'])
  def test_retrieve_items_from_line_4(self):
    result = main.retrieve_items_from_line("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    self.assertEqual(result, ['v'])
  def test_retrieve_items_from_line_5(self):
    result = main.retrieve_items_from_line("ttgJtRGJQctTZtZT")
    self.assertEqual(result, ['t'])
  def test_retrieve_items_from_line_6(self):
    result = main.retrieve_items_from_line("CrZsJsPPZsGzwwsLwLmpwMDw")
    self.assertEqual(result, ['s'])

  def test_priorities_for_array_1(self):
    result = main.priorities_for_array(['a'])
    self.assertEqual(result, 1)
  def test_priorities_for_array_2(self):
    result = main.priorities_for_array(['a', 'A'])
    self.assertEqual(result, 28)
  def test_priorities_for_array_1(self):
    result = main.priorities_for_array(['a'])
    self.assertEqual(result, 1)
  # example from day page
  def test_priorities_for_array_3(self):
    result = main.priorities_for_array(['p', 'L', 'P', 'v', 't', 's'])
    self.assertEqual(result, 157)

  def test_process_array(self):
    test_data = [
      "vJrwpWtwJgWrhcsFMMfFFhFp",
      "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
      "PmmdzqPrVvPwwTWBwg",
      "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
      "ttgJtRGJQctTZtZT",
      "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    result = main.process(test_data)
    self.assertEqual(result, 157)

if __name__ == '__main__':
  unittest.main()