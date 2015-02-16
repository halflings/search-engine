import argparse
import os
import pickle

from index import TfidfIndex
from tokenizing import tokenize_file

def index_dir(directory, index):
    for filename in os.listdir(directory):
        print("Indexing '{}'".format(filename))
        file_path = os.path.join(directory, filename)
        for pos, token in enumerate(tokenize_file(file_path, encoding='latin-1')):
            index.insert(token, file_path, pos)

if __name__ == '__main__':
    # Command-line arguments parsing
    parser = argparse.ArgumentParser(description='Index the given directories.')
    parser.add_argument('dirs', metavar='directory', type=str, nargs='+',
                       help='Directories that need to be indexed')
    parser.add_argument('-index_path', type=str, default='cached_index.pickle',
                       help='Path where the index will be saved.')
    args = parser.parse_args()

    # Opening files and indexing them.
    index = TfidfIndex()
    for directory in args.dirs:
        index_dir(directory, index)
    print("Finished indexing!")

    # Dumping the index to a file
    with open(args.index_path, 'w') as index_file_output:
        pickle.dump(index, index_file_output)