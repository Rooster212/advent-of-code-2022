import unittest
import main

class SimpleTest(unittest.TestCase):

  def test_find_visible_trees(self):
    result = main.find_visible_trees_count([
      "30373",
      "25512",
      "65332",
      "33549",
      "35390",
    ])
    self.assertEqual(result, 21)


if __name__ == '__main__':
  unittest.main()