import os
import logging

from importlib import import_module


class Parser:

    __logger = logging.getLogger(__name__)

    __parser_dir = 'parsers'

    def __init__(self):

        self.__logger.info("base parser class instantiated")

        self.driver = os.getenv("__PARSER_DRIVER__")

    def __call__(self, *args, **kwargs):

        """

            This method will try to instantiate reader class based on the driver defined

            :param args:
            :param kwargs:
            :return: response object

        """

        try:

            self.__logger.info(f"trying to instantiate parser for {self.driver} from {self.__parser_dir}")

            module = import_module(f"{self.__parser_dir}.{self.driver.lower()}_parser")
            class_ = getattr(module, f"{self.driver.capitalize()}Parser")

            return class_()
        except Exception as e:
            self.__logger.exception(f"Error while trying to initialize {e}")
            raise Exception(f"Can't initialize {self.driver.capitalize()}Parser class from {self.__parser_dir} dir")

    @staticmethod
    def handler():

        try:

            parser = Parser()
            return parser().handler()

        except Exception as e:

            raise Exception
