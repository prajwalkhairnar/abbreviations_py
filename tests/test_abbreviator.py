import unittest
from abbreviations_py.textes.abbreviator import fix, update_abbreviations

class TestAbbreviator(unittest.TestCase):
    def test_abbreviate(self):
        input_text = "Hello! gr8 to meet you"
        expected_output = "hello great to meet you"
        self.assertEqual(fix(input_text), expected_output)

    def test_known_abbreviations(self):
    	input_text = "OMG gr8 BRB"
    	expected_output = "oh my god great be right back"
    	self.assertEqual(fix(input_text), expected_output)

    def test_no_abbreviations(self):
        input_text = "This is a normal sentence"
        self.assertEqual(fix(input_text), input_text.lower())

    def test_new_abbreviations(self):
        input_text = "LOL ttyl"
        expected_output = "laugh out loud talk to you later"

        new_mappings = {
            "lol": "laugh out loud",
            "ttyl": "talk to you later"
        }
        update_abbreviations(new_mappings)

        self.assertEqual(fix(input_text), expected_output)

    def test_mixed_case(self):
        input_text = "AbCdEf gr8 TeXt"
        expected_output = "abcdef great text"
        self.assertEqual(fix(input_text), expected_output)

    def test_empty_input(self):
        input_text = ""
        self.assertEqual(fix(input_text), "")

    def test_input_with_punctuations(self):
        input_text = "I'll see you when you're back, ttyl!"
        expected_output = "I will see you when you are back talk to you later"
        self.assertEqual(fix(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
