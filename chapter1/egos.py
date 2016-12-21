import sys
import os
# We retrieve the folder as the first positional argument
# to the command-line call
if len(sys.argv) > 1:
    folder = sys.argv[1]
# We list all files in the specified folder
files = os.listdir(folder)
# ids contains the list of idenfitiers
identifiers = [int(file.split('.')[0]) for file in files]
# Finally, we remove duplicates with set(), and sort the list
# with sorted().
ids = sorted(set(identifiers))