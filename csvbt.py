# csvbt.py
# This file is the main script that processes the csv file and outputs a .js
# file with the json object as a variable called 'data'.
# All logic is taken from csv-process.py

import csv-process.py

# Constants
HELP_TEXT = "There is no help text available, see " \
            "https://github.com/singold/csv-bubbletree for details"

# Main function for CLI
def main():
    
    if "--help" in sys.argv OR "--h" in sys.argv:
	print(HELP_TEXT)
	return

main()
