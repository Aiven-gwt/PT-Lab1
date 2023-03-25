import re
from keysdikt import *


def get_cords_qwer(sim_from_text):
    """
    Функция для получения координат символа из keys_dict

    :параметр sim_from_text: строчный символ для которого нужно получить координвты
    :return: функция фозвращает список с 2-мя элементами, где 0-й элемент это строка, а 1-й - столбец
    """
    for key in keys_dict.keys():
        for value in keys_dict[key]['qwer_key']:
            if value == sim_from_text:
                return [keys_dict[key]['raw'],
                        keys_dict[key]['column']]


def value_passing_fingers_qwerty(column, value):
    """
    Функция для записи шагов пройденных каждым пальцем. Поступает номер колонки и колличество шагов,
    в зависимости от ряда выбирается палец и записывается кол-во шагов

    :параметр column: номер столбца
    :параметр value: колличество шагов которое прошёл палец
    :return: функция ничего не возвращает, а записывает значения в counter_fingers
    """
    match column:
        case 0 | 1:
            counter_fingers_qwer['f5l'] += value
        case 2:
            counter_fingers_qwer['f4l'] += value
        case 3:
            counter_fingers_qwer['f3l'] += value
        case 4 | 5:
            counter_fingers_qwer['f2l'] += value
        case 6 | 7:
            counter_fingers_qwer['f2r'] += value
        case 8:
            counter_fingers_qwer['f3r'] += value
        case 9:
            counter_fingers_qwer['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers_qwer['f5r'] += value


def count_steps_qwerty(first_sim, second_sim):
    """
    Функция для подсчета шагов. При поступлении 2-х символов, считает шаги затраченные на нажатие второго.

    :param first_sim: предыдущий символ текста
    :param second_sim: последующий символ текста
    :return: функция ничего не возвращает, а передаёт значения в функцию для записи шагов value_passing_fingers
    """
    if get_cords_qwer(first_sim)[1] - get_cords_qwer(second_sim)[1] == 0:  # если символы находятся в одном столбце
        value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                     abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]))
        # записываем в словаль колличество шагов в зависимости от разности номеров строк в которые входят элементы
    else:  # если же символы находятся в разных столбцах
        if get_cords_qwer(first_sim)[0] != get_cords_qwer(second_sim)[0]:  # если символы в разных строках
            match get_cords_qwer(second_sim)[1]:  # в зависимости от номеров столбцов записывам кол-во шагов в словарь
                case 5 | 6:  # т.к. 5й и 6й столбцы бьются 1м пальцем(л. или п. указательным)
                    # прибавляем 1 шаг для занятия позиции от home ряда
                    if get_cords_qwer(second_sim)[0] == 2:
                        value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1], 1)
                    else:
                        value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                     abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:  # столбцы бьющиеся 1м пальцем
                    if get_cords_qwer(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                     abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]))
                case 11:  # 11 и 12 бьются п.мезинцем поэтому прибавляем 1 или 2 шага для занятия позиции
                    value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                 abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                 abs(get_cords_qwer(first_sim)[0] - get_cords_qwer(second_sim)[0]) + 2)
        if get_cords_qwer(first_sim)[0] == get_cords_qwer(second_sim)[0]:  # если символы в одинаковых строках
            match get_cords_qwer(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                 abs(get_cords_qwer(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                 abs(get_cords_qwer(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers_qwerty(get_cords_qwer(second_sim)[1],
                                                 abs(get_cords_qwer(second_sim)[0] - 2) + 2)


def main():
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'[^А-Яа-я,*.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    value_passing_fingers_qwerty(0, len(list_upper_case) * 2)
    text = [i.lower() for i in text]
    print(text)
    for i in range(1, len(text)):
        count_steps_qwerty(text[i - 1], text[i])


if __name__ == '__main__':
    main()
