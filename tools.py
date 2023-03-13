"""
Файл для теста составляющих частей программы
"""
# dikt = {1: ['дада', 'нетнет'], 2: ['мбмб', 'хзхз']}
#
# print(dikt[1][1])
# text = 'Ся'
# fingers_dict = dict(f5l={1: '*', 2: '.', 13: 'ц', 26: 'у', 37: 'ф'},
#                     f4l={3: 'ё', 14: 'ь', 27: 'и', 38: 'э'},
#                     f3l={4: 'c', 15: 'я', 28: 'е', 39: 'х'},
#                     f2l={5: '?', 6: '!', 16: ',', 17: '.', 29: 'о', 30: 'а', 40: 'ы', 41: 'ю'},
#                     f1={},
#                     f2r={7: ' ', 8: '-', 18: 'з', 19: 'в', 31: 'л', 32: 'н', 42: 'б', 43: 'м'},
#                     f3r={9: '\'', 20: 'к', 33: 'т', 44: 'п'},
#                     f4r={10: '(', 21: 'д', 34: ']', 45: 'г'},
#                     f5r={11: ')', 12: '_', 22: 'ч', 23: 'ш', 24: 'щ', 25: '"', 35: 'р', 36: 'й', 46: 'ж'})
#
# for i in text:
#     for key, value in fingers_dict.items():


# n = 17
# match n:
#     case 10 | 12 | 13:
#         print('Yes')
#     case 15 | 16 | 17:
#         print('No')
# |||||||||||Вариант при использовании 2х словарей|||||||||||
# with open('text_2.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     text = text.lower()
# text = list(text)
# #print(text)
# list_keys = []
# for i in text:
#     for key, value in keys_dict.items():
#         if keys_dict[key] == i:
#             list_keys.append(key)
# print(list_keys)
# text = 'Ваня'
# text = list(text)
# print(text)
# for i in text:
#     if i.isupper():
#         getterCoords(i.lower())
#     else:
#         getterCoords(i)
# for i in text:
#     for key in keys_dict.keys():
#         for value in keys_dict[key]['skor_key']:
#             if value == i:
#                 print(keys_dict[key]['raw'], 'Строка')
#                 print(keys_dict[key]['column'], 'Столбец')
# for i in range(1, len(text)):
#     print(text[i-1], text[i])
