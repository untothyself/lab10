"""
Program: Word Analyzer
Author: Abass Hassan
Purpose: Reads a text file, counts word amount, and shows the results alphabetically.
Starter Code: None
Date: July 2026
"""

"""
Program: Word Analyzer
Author: Your Name
Purpose: Reads a text file selected by the user, counts the frequency of
each word, and prints the results alphabetically.
Starter Code: None
Date: July 2026
"""

from pathlib import Path
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}