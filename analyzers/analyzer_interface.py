from abc import abstractmethod


class AnalyzerInterface:

    """

        This is base interface for all the analyzer we will build

    """

    def __init__(self):

        self.clean_text: str | None = None
        self.word_counts: dict      = {}

    @abstractmethod
    def get_word_counts(self):

        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def handler(clean_text):

        raise NotImplementedError
