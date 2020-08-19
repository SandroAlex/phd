"""
Script for systematic renaming.
"""

# Load packages.
import sys
import os

# Input arguments.
DIR = sys.argv[1]
old_patt = sys.argv[2]
new_patt = sys.argv[3]

# List all files in directory.
for OLD_FILE in sorted(os.listdir(DIR)):

    # Continue only if the file has the old pattren.
    if old_patt in OLD_FILE:
        
        # Replace old by new pattern.
        NEW_FILE = OLD_FILE.replace(old_patt, new_patt)

        # File paths for source and destination.
        old_file_path = DIR + OLD_FILE
        new_file_path = DIR + NEW_FILE

        # Rename files.
        os.rename(old_file_path, new_file_path)
