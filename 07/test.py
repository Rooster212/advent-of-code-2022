import unittest
import main


class Day07Tests(unittest.TestCase):
    def test_process_command__cd_root(self):
        processor = main.Day07()
        processor.process_command('cd /')
        self.assertEqual(processor.get_pwd_location(), ['/'])

    def test_process_command__cd_down(self):
        processor = main.Day07()
        processor.process_command('cd /')
        processor.process_command('cd e')
        self.assertEqual(processor.get_pwd_location(), ['/', 'e'])

    def test_process_command__cd_up(self):
        processor = main.Day07()
        processor.process_command('cd /')
        processor.process_command('cd e')
        processor.process_command('cd f')
        processor.process_command('cd g')
        processor.process_command('cd ..')
        self.assertEqual(processor.get_pwd_location(), ['/', 'e', 'f'])


if __name__ == '__main__':
    unittest.main()
