from abc import ABC, abstractmethod


class ParserInterface(ABC):

    """

        This is base interface for all the Parsers we will build to load
        the text, Parsers can be defined based on the data source
        i.e. PDFs, WordFiles, WEB, Image, Row Text file ..

    """

    @abstractmethod
    def get_data_source(self):

        raise NotImplementedError

    @abstractmethod
    def extract_text(self):

        raise NotImplementedError
