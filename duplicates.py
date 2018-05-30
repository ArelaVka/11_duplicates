import sys
import os
import argparse
import collections


def list_dir(path):
    dir_info = collections.defaultdict(list)
    for dir, full_dir, file_name in os.walk(path):
        for each_file in file_name:
            full_path = os.path.join(dir, each_file)
            file_size = os.path.getsize(full_path)
            file_info = (each_file, file_size)
            dir_info[file_info].append(full_path)
    return dir_info


def find_duplicates(dir_full_info):
    return [dir_full_info for dir_full_info in dir_full_info.values()
            if len(dir_full_info) > 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find duplicates in '
                                                 'directory recursively')
    parser.add_argument('<directory>', type=str,
                        help='path of scanning directory')
    args = parser.parse_args()

    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        scan_directory = sys.argv[1]
    else:
        sys.exit('You forget enter path or file does not exist.'
                 'Please read help (--help)')
    info = list_dir(scan_directory)
    for each_file, duplicate_file in find_duplicates(info):
        print('\nFile "{0}" is copy of "{1}"'.format(each_file, duplicate_file))
