"""
Program: Word Analyzer
Author: Abass Hassan
Purpose: Reads a text file, counts word amount, and shows the results alphabetically.
Starter Code: None
Date: July 2026
"""

from pathlib import Path
import string


class WordAnalyzer:

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}
    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translator = str.maketrans('', '', string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def print_report(self):
        print()

        for word in sorted(self.__frequencies.keys()):
            print(f"{word:<20} :: {self.__frequencies[word]}")


def main():
    files = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }