import os
import core

from parsers.parser import Parser
from analyzers.analyzer import Analyzer


if __name__ == "__main__":

    """
    
        This is the main entry point of this application
    
    """

    try:

        parser = Parser.handler()
        an = Analyzer.handler(parser.clean_text)

        print(an.word_counts[:10])

    except Exception as e:
        print("Error while to complete the process")
