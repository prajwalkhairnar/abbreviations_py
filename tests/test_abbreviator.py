import unittest
from abbreviations_py.textes.abbreviator import abbreviate, update_abbreviations

class TestAbbreviator(unittest.TestCase):
    def test_abbreviate(self):
        input_text = "Hello! gr8 to meet you"
        expected_output = "hello great to meet you"
        self.assertEqual(abbreviate(input_text), expected_output)

    def test_known_abbreviations(self):
    	input_text = "OMG gr8 BRB"
    	expected_output = "oh my god great be right back"
    	self.assertEqual(abbreviate(input_text), expected_output)

    def test_no_abbreviations(self):
        input_text = "This is a normal sentence"
        self.assertEqual(abbreviate(input_text), input_text.lower())

    def test_new_abbreviations(self):
        input_text = "LOL ttyl"
        expected_output = "laugh out loud talk to you later"

        new_mappings = {
            "LOL": "laugh out loud",
            "TTYL": "talk to you later"
        }
        update_abbreviations(new_mappings)

        self.assertEqual(abbreviate(input_text), expected_output)

    def test_mixed_case(self):
        input_text = "AbCdEf gr8 TeXt"
        expected_output = "abcdef great text"
        self.assertEqual(abbreviate(input_text), expected_output)

    def test_empty_input(self):
        input_text = ""
        self.assertEqual(abbreviate(input_text), "")

    def test_input_with_punctuations(self):
        input_text = "Hello, gr8! How are you?"
        expected_output = "hello great how are you"
        self.assertEqual(abbreviate(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
