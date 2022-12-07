import unittest
import main


class SimpleTest(unittest.TestCase):

  def test_get_upper_lower_1(self):
    result = main.get_upper_lower_as_numbers('2-3')
    self.assertEqual(result, (2, 3))
  def test_get_upper_lower_2(self):
    result = main.get_upper_lower_as_numbers('8-51')
    self.assertEqual(result, (8, 51))

  # Examples from day 4 page
  def test_line_does_fully_overlap_1(self):
    result = main.line_does_fully_overlap('2-4,6-8')
    self.assertEqual(result, False)
  def test_line_does_fully_overlap_2(self):
    result = main.line_does_fully_overlap('2-3,4-5')
    self.assertEqual(result, False)
  def test_line_does_fully_overlap_3(self):
    result = main.line_does_fully_overlap('5-7,7-9')
    self.assertEqual(result, False)
  def test_line_does_fully_overlap_4(self):
    result = main.line_does_fully_overlap('2-8,3-7')
    self.assertEqual(result, True)
  def test_line_does_fully_overlap_5(self):
    result = main.line_does_fully_overlap('6-6,4-6')
    self.assertEqual(result, True)
  def test_line_does_fully_overlap_6(self):
    result = main.line_does_fully_overlap('2-6,4-8')
    self.assertEqual(result, False)

  def test_line_does_overlap_1(self):
    result = main.line_does_overlap('2-4,6-8')
    self.assertEqual(result, False)
  def test_line_does_overlap_2(self):
    result = main.line_does_overlap('2-3,4-5')
    self.assertEqual(result, False)
  def test_line_does_overlap_3(self):
    result = main.line_does_overlap('5-7,7-9')
    self.assertEqual(result, True)
  def test_line_does_overlap_4(self):
    result = main.line_does_overlap('2-8,3-7')
    self.assertEqual(result, True)
  def test_line_does_overlap_5(self):
    result = main.line_does_overlap('6-6,4-6')
    self.assertEqual(result, True)
  def test_line_does_overlap_6(self):
    result = main.line_does_overlap('2-6,4-8')
    self.assertEqual(result, True)

if __name__ == '__main__':
  unittest.main()