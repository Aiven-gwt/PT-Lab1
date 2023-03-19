"""
Файл для сборки программы
"""
# наша раскладка ANT, а не skoropis!!! Стоит переделать skor_key на ant_key,
# а так же добавить 'qwer_key': символ соответствующий qwery-расскладке, так же как прописан
# skor_key(ПРОСТО ДОБАВИТЬ НИЧЕГО НЕ МЕНЯЯ)
keys_dict = {2: {'skor_key': '1', 'raw': 0, 'column': 1},
             3: {'skor_key': '2', 'raw': 0, 'column': 2},
             4: {'skor_key': '3', 'raw': 0, 'column': 3},
             5: {'skor_key': '4', 'raw': 0, 'column': 4},
             6: {'skor_key': '5', 'raw': 0, 'column': 5},
             7: {'skor_key': '6', 'raw': 0, 'column': 6},
             8: {'skor_key': '7', 'raw': 0, 'column': 7},
             9: {'skor_key': '8', 'raw': 0, 'column': 8},
             10: {'skor_key': '9', 'raw': 0, 'column': 9},
             11: {'skor_key': '0', 'raw': 0, 'column': 10},
             12: {'skor_key': '*', 'raw': 0, 'column': 11},
             13: {'skor_key': '=', 'raw': 0, 'column': 12},
             14: {'skor_key': '', 'raw': 0, 'column': 0},
             15: {'skor_key': '', 'raw': 0, 'column': 0},
             16: {'skor_key': 'ц', 'raw': 1, 'column': 1},
             17: {'skor_key': 'ь', 'raw': 1, 'column': 2},
             18: {'skor_key': 'я', 'raw': 1, 'column': 3},
             19: {'skor_key': ',', 'raw': 1, 'column': 4},
             20: {'skor_key': '.', 'raw': 1, 'column': 5},
             21: {'skor_key': 'з', 'raw': 1, 'column': 6},
             22: {'skor_key': 'в', 'raw': 1, 'column': 7},
             23: {'skor_key': 'к', 'raw': 1, 'column': 8},
             24: {'skor_key': 'д', 'raw': 1, 'column': 9},
             25: {'skor_key': 'ч', 'raw': 1, 'column': 10},
             26: {'skor_key': 'ш', 'raw': 1, 'column': 11},
             27: {'skor_key': 'щ', 'raw': 1, 'column': 12},
             28: {'skor_key': '', 'raw': 0, 'column': 0},
             29: {'skor_key': '', 'raw': 0, 'column': 0},
             30: {'skor_key': 'у', 'raw': 2, 'column': 1},
             31: {'skor_key': 'и', 'raw': 2, 'column': 2},
             32: {'skor_key': 'е', 'raw': 2, 'column': 3},
             33: {'skor_key': 'о', 'raw': 2, 'column': 4},
             34: {'skor_key': 'а', 'raw': 2, 'column': 5},
             35: {'skor_key': 'л', 'raw': 2, 'column': 6},
             36: {'skor_key': 'н', 'raw': 2, 'column': 7},
             37: {'skor_key': 'т', 'raw': 2, 'column': 8},
             38: {'skor_key': 'с', 'raw': 2, 'column': 9},
             39: {'skor_key': 'р', 'raw': 2, 'column': 10},
             40: {'skor_key': 'й', 'raw': 2, 'column': 11},
             41: {'skor_key': 'ё', 'raw': 0, 'column': 0},
             42: {'skor_key': '', 'raw': 0, 'column': 0},
             43: {'skor_key': '', 'raw': 0, 'column': 0},
             44: {'skor_key': 'ф', 'raw': 3, 'column': 1},
             45: {'skor_key': 'э', 'raw': 3, 'column': 2},
             46: {'skor_key': 'х', 'raw': 3, 'column': 3},
             47: {'skor_key': 'ы', 'raw': 3, 'column': 4},
             48: {'skor_key': 'ю', 'raw': 3, 'column': 5},
             49: {'skor_key': 'б', 'raw': 3, 'column': 6},
             50: {'skor_key': 'м', 'raw': 3, 'column': 7},
             51: {'skor_key': 'п', 'raw': 3, 'column': 8},
             52: {'skor_key': 'г', 'raw': 3, 'column': 9},
             53: {'skor_key': 'ж', 'raw': 3, 'column': 10},
             54: {'skor_key': '', 'raw': 0, 'column': 0},
             55: {'skor_key': '', 'raw': 0, 'column': 0},
             56: {'skor_key': '', 'raw': 0, 'column': 0},
             57: {'skor_key': ' ', 'raw': 0, 'column': 0},
             58: {'skor_key': '~', 'raw': 2, 'column': 1}}

counter_fingers = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0, 'f5r': 0}


# функция для получения номера строки и столбца определённого символа из словаря keys_dict


def get_cords(sim_from_text):
    for key in keys_dict.keys():
        for value in keys_dict[key]['skor_key']:
            if value == sim_from_text:
                return [keys_dict[key]['raw'],
                        keys_dict[key]['column']]  # первый элемент возвращаемого списка - строка, второй - столбец


# функция для записи шагов пройденных каждым пальцем. Поступает номер колонки и колличество шагов,
# в зависимости от ряда выбирается палец и записывается кол-во шагов


def value_passing_fingers(column, value):
    match column:
        case 0 | 1:
            counter_fingers['f5l'] += value
        case 2:
            counter_fingers['f4l'] += value
        case 3:
            counter_fingers['f3l'] += value
        case 4 | 5:
            counter_fingers['f2l'] += value
        case 6 | 7:
            counter_fingers['f2r'] += value
        case 8:
            counter_fingers['f3r'] += value
        case 9:
            counter_fingers['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers['f5r'] += value


# функция для подсчета шагов. При поступлении 2-х символов, считает шаги затраченные на нажатие второго.


def count_steps(first_sim, second_sim):
    if get_cords(first_sim)[1] - get_cords(second_sim)[1] == 0:  # если символы находятся в одном столбце
        value_passing_fingers(get_cords(second_sim)[1], abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
        # записываем в словаль колличество шагов в зависимости от разности номеров строк в которые входят элементы
    else:  # если же символы находятся в разных столбцах
        if get_cords(first_sim)[0] != get_cords(second_sim)[0]:  # если символы в разных строках
            match get_cords(second_sim)[1]:  # в зависимости от номеров столбцов записывам кол-во шагов в словарь
                case 5 | 6:  # т.к. 5й и 6й столбцы бьются 1м пальцем(л. или п. указательным)
                    # прибавляем 1 шаг для занятия позиции от home ряда
                    if get_cords(second_sim)[0] == 2:
                        value_passing_fingers(get_cords(second_sim)[1], 1)
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:  # столбцы бьющиеся 1м пальцем
                    if get_cords(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
                case 11:  # 11 и 12 бьются п.мезинцем поэтому прибавляем 1 или 2 шага для занятия позиции
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 2)
        if get_cords(first_sim)[0] == get_cords(second_sim)[0]:  # если символы в одинаковых строках
            match get_cords(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 2)


if __name__ == '__main__':
    text = ['~', 'ц', 'щ']
    for i in range(1, len(text)):
        count_steps(text[i-1], text[i])
    print(counter_fingers)