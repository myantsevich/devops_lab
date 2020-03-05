import os
from datetime import datetime

# output files only from the parent directory
basepath = '..'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)


# list files recursively
def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
            elif entry.is_dir():
                list_files(entry.path)


list_files('.')

# filter by file extension
for file_name in os.listdir('.'):
    if file_name.endswith('.py'):
        print(file_name)

# order output by filename
mylist = []


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                mylist.append(str(entry.name))
                mylist.sort()
            elif entry.is_dir():
                list_files(entry.path)


list_files('.')
print("\n".join(str(x) for x in mylist))


# order output by date of creation


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def list_files(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                info = entry.stat()
                print(f'{convert_date(info.st_mtime)}\t {entry.name} ')
            elif entry.is_dir():
                list_files(entry.path)


list_files('.')