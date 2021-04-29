# 1. Дан список строк my_list. Создать новый список в который поместить элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
# my_list = ["qwe", "rty", "uio"]
# new_list = []
# for index in range(len(my_list)):
#     value = my_list[index]
#     if not index % 2:
#         value = value[::-1]
#     new_list.append(value)
# print(new_list)

# Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# my_list = ["abc", "qwe", "aaa", "aaaaaaaaa"]
# new_list = []
# for string in my_list:
#     if string[0] == "a":
#         new_list.append(string)
# print(new_list)

# Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# my_list = ["abc", "qwe", "aaa", "baaaaaaaaa"]
# new_list = []
# for string in my_list:
#     if "a" in string:
#         new_list.append(string)
# print(new_list)

# Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
# my_list = ["abc", "qwe", "aaa", "baaaaaaaaa", 77, 42]
# new_list = []
# for value in my_list:
#     if type(value) == str:
#         new_list.append(value)
# print(new_list)

# Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
# my_str = "Where is my mind?"
# my_list = []
# my_set = set(my_str)
# for symbol in my_set:
#     if my_str.lower().count(symbol) == 1:
#         my_list.append(symbol)
# print(my_list)


# Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# my_str = "Where is my mind?"
# my_str_1 = "See it swimming"
#
# my_set = set(my_str)
# my_set_1 = set(my_str_1)
# for symbol in my_set.intersection(my_set_1):
#     my_list.append(symbol)
# print(my_list)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
# my_str = "I like booo"
# my_str_1 = "I like wooo"
# my_list = []
# my_set = set(my_str)
# my_set_1 = set(my_str_1)
# for symbol in my_set.intersection(my_set_1):
#     if my_str_1.lower().count(symbol) == 1 and my_str.lower().count(symbol) == 1:
#         my_list.append(symbol)
# print(my_list)






#
# for symbols in my_final_set:
#     my_list.append(symbols)
# print(my_list)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

# person = {"name": "John",
#           "surname":"Smith",
#           "age": 23,
#           "job": {"employment": True,
#                   "position":"doctor"},
#           "address": {"country": "Ukraine",
#                       "city": "Dnipro",
#                       "street": "Polya"}}
#
# print(person["address"]["country"])
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
# cake = {"layers": {"flour": "300g", "milk": "500g", "butter":"600g", "eggs":2},
#         "cream": {"sugar": "200g", "butter":"300g", "vanila":"5g", "sour-cream":"260g"},
#         "icing": {"cocoa": "50g", "sugar": "100g", "butter": "120g"}}



