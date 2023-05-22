import os
import core

from parsers.parser import Parser
from analyzers.analyzer import Analyzer

from helpers.utils import save_results


if __name__ == "__main__":

    """
    
        This is the main entry point of this application
    
    """

    try:

        text_analyzer = Analyzer.handler(Parser.handler())

        print(text_analyzer.word_counts[:10])

        save_results(text_analyzer.word_counts)
    except Exception as e:
        print(e)
        print("Error while to complete the process")
