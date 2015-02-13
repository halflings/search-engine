import argparse
import os


if __name__ == '__main__':
    # Command-line arguments parsing
    parser = argparse.ArgumentParser(description='Index the given directories.')
    parser.add_argument('dirs', metavar='directory', type=str, nargs='+',
                       help='Directories that need to be indexed')
    args = parser.parse_args()

    # Opening files and indexing them. WIP.
    for directory in args.dirs:
        for path in os.listdir(directory):
            with open(os.path.join(directory, path)) as indexed_file:
                print indexed_file