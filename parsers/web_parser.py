import re
import logging
import requests

from parsers.cleaner import HTMLCleaner
from parsers.parser_interface import ParserInterface


class WebParser(ParserInterface):

    """

        This is web parser, this call will take url and input from
        user and try to extract the text from the given URL.

    """

    __logger = logging.getLogger(__name__)

    def __init__(self):

        self.source: str | None     = None
        self.row_text: str | None   = None

        super(WebParser, self).__init__()

    def get_data_source(self, message: str = "Enter WEB URL:: "):

        """

            This method will try to get source url from user

            :param message:
            :return:

        """

        try:

            self.source = input(message)
            self.validater()

            return self
        except Exception as e:
            WebParser.__logger.exception(f"Error while trying to get the data source from user {e}")
            raise Exception

    def validater(self):

        """

            This method will try to validate the user input and check
            if the provided input is a valid URL or not

            :return:

        """

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

        """

            This method will try to extract the text form the provided URL

            :return:

        """

        try:

            response = requests.get( url = self.source )

            if response.status_code == 200:

                self.row_text = response.text

            if not response.status_code == 200:

                raise Exception("Data not found")

            return self
        except Exception as e:

            raise Exception

    @staticmethod
    def handler():

        """

            This function will handle the process of text
            extraction from the user provided URL.

            :return:

        """

        try:

            parser = WebParser().get_data_source().extract_text()
            clean_text = HTMLCleaner.clean(parser.row_text)
            return clean_text

        except Exception as e:

            raise Exception
