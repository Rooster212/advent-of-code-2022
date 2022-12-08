import unittest
import main


class SimpleTest(unittest.TestCase):

    def get_test_stacks(self):
        # I have reversed these to work for testing
        stacks = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P'],
        ]
        return stacks

    def get_test_steps(self):
        return [
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
        ]

    def test_get_challenge_input_stacks(self):
        result = main.get_challenge_input_stacks()
        self.assertEqual(len(result), 9)

    def test_step_parse_1(self):
        result = main.step_parse('move 1 from 2 to 3')
        self.assertEqual(result, (1, 2, 3))

    def test_step_parse_2(self):
        result = main.step_parse('move 5 from 12 to 51')
        self.assertEqual(result, (5, 12, 51))

    def test_step_parse_3(self):
        result = main.step_parse('move 15 from 2 to 13')
        self.assertEqual(result, (15, 2, 13))

    def test_run(self):
        stacks = self.get_test_stacks()
        steps = self.get_test_steps()
        result = main.process_stacks_and_steps(stacks, steps)
        main.print_stacks(result)


if __name__ == '__main__':
    unittest.main()
