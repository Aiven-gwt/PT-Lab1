import re


def main():
    text = input('Введите слова: ')
    text = text.lower()
    text = re.sub(r'[^а-я,*.?!\-_\'()" \s]', '', text)
    print(text)

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
                 58: {'skor_key': '', 'raw': 0, 'column': 0}}
    text = list(text)
    for i in text:
        for key, value in keys_dict.items():
            if keys_dict[key] == i:
                print(key, ' ', i)


if __name__ == '__main__':
    main()
