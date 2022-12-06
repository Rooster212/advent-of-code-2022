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

  def test_calculateline(self):
    result = main.retrieve_items_from_line("vJrwpWtwJgWrhcsFMMfFFhFp")
    print(result)

if __name__ == '__main__':
  unittest.main()