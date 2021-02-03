import os
import sys
from datetime import datetime
from time import time
import json
from additions.json_template import fill_template
from additions.graph import create_gif, get_values


START_TIME = time()
PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + '/animations'

if not os.path.exists(PATH):
    os.mkdir(PATH)


def get_time():
    return datetime.now().strftime('/%d.%m.%Y %H:%M:%S')


def append_file(path=PATH, now=get_time()):
    path_to_file = path + now
    os.mkdir(path_to_file)
    file = open(f'{path_to_file}/info.txt', 'w')
    create_gif(now)
    return writing_procedure(file, now)


def writing_procedure(file, now):
    for symbol in json.dumps(fill_template(now, time()-START_TIME, get_values()), indent=4):
        file.write(symbol)
    else:
        file.close()


if __name__ == '__main__':
    append_file()

