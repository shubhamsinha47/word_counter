from analyzers.analyzer_interface import AnalyzerInterface


class PythonBasedAnalyzer(AnalyzerInterface):

    def __init__(self):

        super(PythonBasedAnalyzer, self).__init__()

        self.clean_text: str | None = None
        self.word_counts: dict      = {}

    def get_clean_text(self, text: str):

        self.clean_text = text

        return self

    def get_word_counts(self):

        words = self.clean_text.lower().split()

        for word in words:

            self.word_counts[word] = self.word_counts.get(word, 0) + 1

        self.sort_word_vector()

        return self

    def sort_word_vector(self):

        self.word_counts = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)

        return self

    @staticmethod
    def handler(clean_text):

        try:

            return PythonBasedAnalyzer().get_clean_text(clean_text).get_word_counts()

        except Exception as e:

            raise Exception
