import unittest
from unittest.mock import MagicMock

from parsers.cleaner import HTMLCleaner
from analyzers.python_based_analyzer import PythonBasedAnalyzer


class TextAnalyzerTestCase(unittest.TestCase):

    def test_analyze_html(self):

        text = "<html><h1>shubham, Hello World.</h1>" \
               "<p>Testing the html based text analyzer</p>" \
               "<p>this html shubham</p>" \
               "</html>"

        expected_word_counts = [('shubham', 2), ('html', 2), ('hello', 1), ('world', 1), ('testing', 1), ('based', 1), ('text', 1), ('analyzer', 1)]

        clean_text = HTMLCleaner.clean(text)
        counter = PythonBasedAnalyzer.handler(clean_text)
        self.assertEqual(counter.word_counts[:10], expected_word_counts)

    def test_analyze_text(self):

        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
               "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
               "when an unknown printer took a galley of type and scrambled it to make a type specimen book. " \
               "It has survived not only five centuries, but also the leap into electronic typesetting, " \
               "remaining essentially unchanged. It was popularised in the 1960s with the release of " \
               "Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
               "software like Aldus PageMaker including versions of Lorem Ipsum."

        expected_word_counts = [
            ('lorem', 4), ('ipsum', 4), ('of', 4), ('and', 3), ('it', 3), ('dummy', 2), ('text', 2),
            ('typesetting', 2), ('has', 2), ('a', 2), ('type', 2), ('with', 2), ('simply', 1),
            ('printing', 1), ('industry', 1), ('been', 1), ('industrys', 1), ('standard', 1),
            ('ever', 1), ('since', 1), ('1500s', 1), ('when', 1), ('an', 1), ('unknown', 1),
            ('printer', 1), ('took', 1), ('galley', 1), ('scrambled', 1), ('to', 1), ('make', 1),
            ('specimen', 1), ('book', 1), ('survived', 1), ('not', 1), ('only', 1), ('five', 1),
            ('centuries', 1), ('but', 1), ('also', 1), ('leap', 1), ('into', 1), ('electronic', 1),
            ('remaining', 1), ('essentially', 1), ('unchanged', 1), ('was', 1), ('popularised', 1),
            ('in', 1), ('1960s', 1), ('release', 1), ('letraset', 1), ('sheets', 1),
            ('containing', 1), ('passages', 1), ('more', 1), ('recently', 1), ('desktop', 1),
            ('publishing', 1), ('software', 1), ('like', 1), ('aldus', 1), ('pagemaker', 1),
            ('including', 1), ('versions', 1)
        ]

        clean_text = HTMLCleaner.clean(text)
        counter = PythonBasedAnalyzer.handler(clean_text)
        self.assertEqual(counter.word_counts[:10], expected_word_counts[:10])


if __name__ == '__main__':
    unittest.main()
