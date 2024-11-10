"""Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
    Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после
записи каждого на 0.1 секунду.
    Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:"""

import threading
from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name): # word_count - количество записываемых слов,
                                        # file_name - название файла, куда будут записываться слова.
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Какое-то слово №  {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

# Взятие текущего времени
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# вычисление текущего времени
time_stop = datetime.now()
time_res = time_stop - time_start
print(f'Время выполнения записи в файлы {time_res} секунд')

"""Примечания:
Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки работали почти одновременно."""