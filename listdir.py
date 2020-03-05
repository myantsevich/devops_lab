import os
from datetime import datetime
import argparse


def parent_dir():
    for file_name in os.listdir('..'):
        if os.path.isfile(os.path.join('..', file_name)):
            print(file_name)


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
            elif entry.is_dir():
                list_files(entry.path)


def extension(ext):
    ext = '.', ext
    for file_name in os.listdir('.'):
        if file_name.endswith(ext):
            print(file_name)


def sort_name(path):
    mylist = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                mylist.append(str(entry.name))
                mylist.sort()
            elif entry.is_dir():
                sort_name(entry.path)
    print("\n".join(str(x) for x in mylist))


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def sort_date(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                info = entry.stat()
                print(f'{convert_date(info.st_mtime)}\t {entry.name} ')
            elif entry.is_dir():
                sort_date(entry.path)


parser = argparse.ArgumentParser()
parser.add_argument("--p", help='Output files from parent directory',
                    default=False, action='store_true')
parser.add_argument("--lf", help='List files recursively', default=False,
                    action='store_true')
parser.add_argument("--e", help='Filter by file extension', default='py', type=str,
                    const=1, nargs='?')
parser.add_argument("--sort", help='Sort files by name or date', default=False,
                    choices=['name', 'date'], const=1,
                    nargs='?')
parser.add_argument("--version", action="version", help="Version", version='v0.1')
args = parser.parse_args()

if args.p:
    print('Your parent dir contents the following:')

if args.lf:
    print('Here is all files from this dir and child dirs:')
    list_files('.')

if args.e:
    print('Here is all files with extension:')
    extension(args.e)

if args.sort == 'name':
    print('Here is all files sorted by name:')
    sort_name('.')

else:
    print('Here is all files sorted by date:')
    sort_date('.')
