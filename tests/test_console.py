import unittest
from unittest.mock import patch, MagicMock
from your_module_name import parse, HBNBCommand

class TestParseFunction(unittest.TestCase):
    def test_parse_with_curly_braces(self):
        result = parse("command {arg}")
        self.assertEqual(result, ['command', '{arg}'])

    def test_parse_with_brackets(self):
        result = parse("command [arg]")
        self.assertEqual(result, ['command', '[arg]'])

    def test_parse_with_multiple_commands(self):
        result = parse("command1 [arg1] command2 {arg2}")
        self.assertEqual(result, ['command1 [arg1] command2', '{arg2}'])

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.cmd.storage = MagicMock()

    def test_do_create_missing_class_name(self):
        with patch('builtins.print') as mock_print:
            self.cmd.do_create('')
            mock_print.assert_called_with("** class name missing **")

    def test_do_create_invalid_class_name(self):
        with patch('builtins.print') as mock_print:
            self.cmd.do_create('InvalidClass')
            mock_print.assert_called_with("** class doesn't exist **")

    def test_do_create_valid_class_name(self):
        with patch('builtins.print') as mock_print:
            self.cmd.do_create('BaseModel')
            self.cmd.storage.save.assert_called()

    def test_do_show_missing_class_name(self):
        with patch('builtins.print') as mock_print:
            self.cmd.do_show('')
            mock_print.assert_called_with("** class name missing **")

    # More tests for other command methods

    def test_do_quit(self):
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_EOF(self):
        with patch('builtins.print') as mock_print:
            self.cmd.do_EOF('')
            mock_print.assert_called_with("")

    def test_prompt(self):
        self.assertEqual(self.cmd.prompt, "(hbnb) ")

    def test_emptyline(self):
        self.assertIsNone(self.cmd.emptyline())

if __name__ == '__main__':
    unittest.main()
