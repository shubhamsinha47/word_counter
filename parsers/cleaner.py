import re
import string


class Cleaner:

    """

        This is a base cleaner class

    """

    def __init__(self, row_text):

        self.row_text: str = row_text
        self.clean_text: str | None = None
        self.stop_words: list = ['the', 'is', 'are', 'this']

    def add_stop_words(self, words):

        self.stop_words.extend(words)

        return self

    def remove_punctuation(self):

        self.clean_text = self.clean_text.translate(str.maketrans('', '', string.punctuation))

        return self

    def remove_extra_space(self):

        self.clean_text = " ".join(self.clean_text.strip().split())

        return self

    def remove_stop_words(self):

        words = []

        for word in self.clean_text.lower().split():

            if word not in self.stop_words:

                words.append(word)

        self.clean_text = ' '.join(words)

        return self


class HTMLCleaner(Cleaner):

    def __init__(self, row_text):

        super(HTMLCleaner, self).__init__(row_text)

    @staticmethod
    def clean(row_text: str, stop_words: list = []):

        try:

            cleaner = HTMLCleaner(row_text).add_stop_words(stop_words)\
                .remove_tags().remove_punctuation().remove_stop_words()

            return cleaner.clean_text

        except Exception as e:

            raise Exception('Error while trying to clean the text')

    def remove_tags(self):

        self.clean_text = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', self.row_text,
                                 flags=re.DOTALL)
        self.clean_text = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', self.clean_text,
                                 flags=re.DOTALL)
        self.clean_text = re.sub('<.*?>', ' ', self.clean_text)

        return self
