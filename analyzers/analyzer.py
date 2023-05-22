import os
import logging

from importlib import import_module


class Analyzer:

    __logger = logging.getLogger(__name__)

    __analyzer_dir = 'analyzers'

    def __init__(self):

        self.__logger.info("base analyzer class instantiated")

        self.driver = os.getenv("__ANALYZER__")

    def __call__(self, *args, **kwargs):

        """

            This method will try to instantiate analyzer class based on the driver defined

            :param args:
            :param kwargs:
            :return: response object

        """

        try:

            self.__logger.info(f"trying to instantiate analyzer for {self.driver} from {self.__analyzer_dir}")

            module = import_module(f"{self.__analyzer_dir}.{self.driver.lower()}_based_analyzer")
            class_ = getattr(module, f"{self.driver.capitalize()}BasedAnalyzer")

            return class_()
        except Exception as e:
            self.__logger.exception(f"Error while trying to initialize {e}")
            raise Exception(f"Can't initialize {self.driver.capitalize()}BasedAnalyzer class from {self.__analyzer_dir} dir")

    @staticmethod
    def handler(clean_text):

        try:

            analyzer = Analyzer()
            return analyzer().handler(clean_text)

        except Exception as e:

            raise Exception
