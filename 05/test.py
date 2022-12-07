import unittest
import main


class SimpleTest(unittest.TestCase):

  def test_get_challenge_input_stacks(self):
    result = main.get_challenge_input_stacks()
    self.assertEqual(len(result), 9)


if __name__ == '__main__':
  unittest.main()