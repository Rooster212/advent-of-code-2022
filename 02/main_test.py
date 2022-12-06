import unittest
import rps


class SimpleTest(unittest.TestCase):

  # Returns True or False. 
  def test_draw(self):
    result = rps.calculate('A', 'X')
    self.assertEqual(result, 'draw')

if __name__ == '__main__':
  unittest.main()