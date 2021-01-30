import os
import sys
from datetime import datetime
from time import time
import json

# Импорт нашего шаблона, некоторая информация уже туда записывается, ну короче, все прочитаешь уже внутри файла
from additions.json_template import fill_template

'''
    Короче, работает достаточно быстро, конечно, пока мы не добавили расчеты
    Если требуется что-то добавить, пиши. Попытаюсь ответить в удобное время, хе-хе
'''

# Время старта, нужно для джейсона
START_TIME = time()

# Путь к директории
PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + '/animations'

# Ну тут должно быть понятно, просто создаем директорию animations, если ее нет
if not os.path.exists(PATH):
    os.mkdir(PATH)


# Получение времени нужного формата для создания директории с тем же названием
# Не стал юзать START_TIME, ибо она выдает, как помню, только время, когда нужна и дата также
# Секунды в названии директории добавлены чисто потому, чтобы избежать ошибок,
# мало ли кто-то умудрится запустить скрипт несколько раз в одну минуту :D
def get_time():
    return datetime.now().strftime('/%d.%m.%Y %H:%M:%S')


# функция добавления файла в нужную нам директорию
def append_file(path=PATH, now=get_time()):
    path_to_file = path + now
    os.mkdir(path_to_file)
    file = open(f'{path_to_file}/info.txt', 'w')
    return writing_procedure(file, now)


# Небольшая процедурка, которая записывает наш джейсон в текстовик
def writing_procedure(file, now):
    for symbol in json.dumps(fill_template(now, time()-START_TIME), indent=4):
        file.write(symbol)
    else:
        file.close()


# Ну тут итак все понятно
if __name__ == '__main__':
    append_file()
