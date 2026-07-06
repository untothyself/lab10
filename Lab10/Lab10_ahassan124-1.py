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
    
    script_dir = Path(__file__).parent 

    
    files = {
        "1": script_dir / "princess_mars.txt",
        "2": script_dir / "Tarzan.txt",
        "3": script_dir / "treasure_island.txt",
        "4": script_dir / "monte_cristo.txt"
    }
    while True:

        print("\n--- Word Analyzer ---")
        print("1. Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in files:
            print("Invalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue

        analyzer = WordAnalyzer(files[choice])

        print(f"\nProcessing '{files[choice].name}'...\n")

        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")

main()