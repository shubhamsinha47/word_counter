import re
import string
import logging
import requests

from parsers.parser_interface import ParserInterface


class WebParser(ParserInterface):

    __logger = logging.getLogger(__name__)

    def __init__(self):

        self.source: str | None     = None
        self.row_text: str | None   = None

        super(WebParser, self).__init__()

    def get_data_source(self, message: str = "Enter WEB URL:: "):

        try:

            self.source = input(message)
            self.validater()

            return self
        except Exception as e:
            WebParser.__logger.exception(f"Error while trying to get the data source from user {e}")
            raise Exception

    def validater(self):

        try:

            url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

            check = re.match(url_pattern, self.source)

            if not check:

                self.get_data_source("Please provide a valid URL:: ")

            return self

        except Exception as e:

            WebParser.__logger.exception(f"Error while trying to validate the user provided URL {e}")

            self.get_data_source("Please provide a valid URL:: ")

    def extract_text(self):

        try:

            response = requests.get( url = self.source )

            if response.status_code == 200:

                self.row_text = response.text

            if response.status_code == 404:

                raise Exception("Data not found")

            return self
        except Exception as e:

            raise Exception

    def clean_row_text(self):

        if self.row_text:

            self.remove_html_tags().remove_punctuation().remove_extra_space()

        return self

    def remove_html_tags(self):

        self.clean_text = re.sub('<.*?>', '', self.row_text)

        return self

    def remove_punctuation(self):

        self.clean_text = self.clean_text.translate(str.maketrans('', '', string.punctuation))

        return self

    def remove_extra_space(self):

        self.clean_text = " ".join(self.clean_text.strip().split())

        return self

    @staticmethod
    def handler():

        try:

            parser = WebParser().get_data_source().extract_text().clean_row_text()

            return parser

        except Exception as e:

            raise Exception
