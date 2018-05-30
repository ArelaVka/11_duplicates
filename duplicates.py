import re
import sys
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find duplicates in '
                                                 'directory recursively')
    parser.add_argument('<directory>', type=str,
                        help='path of scanning directory')
    args = parser.parse_args()

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        scan_directory = sys.argv[1]
        names = os.listdir(scan_directory)
        for name in names:
            fullname = os.path.join(scan_directory, name)
            print(fullname)
    else:
        sys.exit('You forget enter path or file does not exist.'
                 'Please read help (--help)')
