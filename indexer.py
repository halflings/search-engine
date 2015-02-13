import argparse
import os

from indexing import tokenize_file

if __name__ == '__main__':
    # Command-line arguments parsing
    parser = argparse.ArgumentParser(description='Index the given directories.')
    parser.add_argument('dirs', metavar='directory', type=str, nargs='+',
                       help='Directories that need to be indexed')
    args = parser.parse_args()

    # Opening files and indexing them. WIP.
    index = dict()
    for directory in args.dirs:
        for filename in os.listdir(directory):
            index[filename] = set()
            print "Indexing '{}'".format(filename)
            file_path = os.path.join(directory, filename)
            for token in tokenize_file(file_path, encoding='latin-1'):
                index[filename].add(token)