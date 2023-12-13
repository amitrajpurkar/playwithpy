import unittest
from io import StringIO
from unittest.mock import patch

from exercise import try_exercise02

class TestTryExercise02(unittest.TestCase):

    @patch('builtins.input', return_value='Hello world')
    def test_estimate_words(self, mock_input):
        expected_output = "Estimated 2 words in 'Hello world'"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            try_exercise02()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='This is a sentence')
    def test_estimate_words_sentence(self, mock_input):
        expected_output = "Estimated 4 words in 'This is a sentence'"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            try_exercise02()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch('builtins.input', return_value='   ')
    def test_estimate_words_empty_string(self, mock_input):
        expected_output = "Estimated 0 words in '   '"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            try_exercise02()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()