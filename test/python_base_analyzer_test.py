import unittest
from unittest.mock import MagicMock

from parsers.cleaner import HTMLCleaner
from analyzers.python_based_analyzer import PythonBasedAnalyzer


class TextAnalyzerTestCase(unittest.TestCase):

    def setUp(self):

        self.cleaner = HTMLCleaner
        self.analyzer = PythonBasedAnalyzer()

    def test_analyze_text(self):
        text = "<html><h1>shubham, Hello World.</h1><p>Testing the html based text analyzer</p><p>this html shubham</p></html>"
        expected_word_counts = {1}

        pass


if __name__ == '__main__':
    unittest.main()