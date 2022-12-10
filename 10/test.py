import unittest
import main


class Day10Tests(unittest.TestCase):
    def get_test_commands(self):
        with open("test_input.txt") as f:
            return f.read().splitlines()

    def test_processor_1(self):
        commands = ["noop", "addx 3", "addx -5"]
        history = main.run_commands(commands)
        self.assertEqual(history[1], {
            'clock': 1,
            'x': 1,
            'signal_strength': 1
        })
        self.assertEqual(history[4], {
            'clock': 4,
            'x': 4,
            'signal_strength': 16
        })
        self.assertEqual(history[6], {
            'clock': 6,
            'x': -1,
            'signal_strength': -6
        })

    def test_processor_2(self):
        commands = self.get_test_commands()
        history = main.run_commands(commands)
        self.assertEqual(history[20], {
            'clock': 20,
            'x': 21,
            'signal_strength': 420
        })
        self.assertEqual(history[60], {
            'clock': 60,
            'x': 19,
            'signal_strength': 1140
        })
        self.assertEqual(history[100], {
            'clock': 100,
            'x': 18,
            'signal_strength': 1800
        })
        self.assertEqual(history[140], {
            'clock': 140,
            'x': 21,
            'signal_strength': 2940
        })
        self.assertEqual(history[180], {
            'clock': 180,
            'x': 16,
            'signal_strength': 2880
        })
        self.assertEqual(history[220], {
            'clock': 220,
            'x': 18,
            'signal_strength': 3960
        })
        target_signal_strengths = [20, 60, 100, 140, 180, 220]

        sum_signal_strength = 0
        for t in target_signal_strengths:
            sum_signal_strength += history[t]['signal_strength']

        self.assertEqual(sum_signal_strength, 13140)

    # def test_processor_1(self):
    #     # processor = main.Day10CommandProcessor(report_every=None)

    #     # test_commands = self.get_test_commands()
    #     # processor.run_commands(test_commands)

    #     # for entry in processor.history:
    #     #     print(processor.history[entry])
    #     # print(processor.history[60])
    #     # print(processor.history[100])
    #     # print(processor.history[140])
    #     # print(processor.history[180])
    #     # print(processor.history[220])


if __name__ == '__main__':
    unittest.main()
