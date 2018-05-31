import sys
import os
import argparse
import collections


def list_dir(path):
    dir_info = collections.defaultdict(list)
    for current_dir, full_dir, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.join(current_dir, file_name)
            file_size = os.path.getsize(full_path)
            file_info = (file_name, file_size)
            dir_info[file_info].append(full_path)
    return dir_info


def find_duplicates(dir_full_info):
    for duplicate_file, path_of_duplicate in dir_full_info.items():
        if len(path_of_duplicate) > 1:
            print('\nDuplicate files:')
            for name in path_of_duplicate:
                print('+', name)


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        scan_directory = sys.argv[1]
    else:
        sys.exit('You forget enter path or file does not exist')
    directory_info = list_dir(scan_directory)
    find_duplicates(directory_info)
