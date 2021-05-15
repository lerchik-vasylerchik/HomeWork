import random
import string


# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# def str_creator(my_list):
#     for index in range(len(my_list)):
#         value = my_list[index]
#         if not index % 2:
#             value = value[::-1]
#         new_list.append(value)
#     return new_list
#
# my_list = ["qwe", "rty", "uio"]
# new_list = []
# print(str_creator(my_list))
#2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
# def list_creator(my_list):
#     for string in my_list:
#         if string[0] == "a":
#             new_list.append(string)
#     return(new_list)
#
# my_list = ["abc", "qwe", "aaa", "aaaaaaaaa"]
# new_list = []
# print(list_creator(my_list))

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# def new_list_creator(my_list):
#     for string in my_list:
#         if "a" in string:
#             new_list.append(string)
#     return new_list
#
#
# my_list = ["abc", "qwe", "aaa", "baaaaaaaaa"]
# new_list = []
# print(new_list_creator(my_list))
#
# 4.Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
# def new_list_creator(my_list):
#     for value in my_list:
#         if type(value) == str:
#             new_list.append(value)
#     return (new_list)
#
#
#
# my_list = ["abc", "qwe", "aaa", "baaaaaaaaa", 77, 42]
# new_list = []
# print(new_list_creator(my_list))

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
# def new_list_creator(my_str):
#     for symbol in my_set:
#         if my_str.lower().count(symbol) == 1:
#             my_list.append(symbol)
#     return(my_list)
#
#
# my_str = "Where is my mind?"
# my_list = []
# my_set = set(my_str)
# print(new_list_creator(my_str))

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

# def new_list_creator(my_str, my_str_1):
#     my_set = set(my_str)
#     my_set_1 = set(my_str_1)
#     for symbol in my_set.intersection(my_set_1):
#         my_list.append(symbol)
#     return (my_list)
#
# my_str = "Where is my mind?"
# my_str_1 = "See it swimming"
# my_list = []
# print(new_list_creator(my_str, my_str_1))

# 7.Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
# def new_list_creator(my_str, my_str_1):
#     my_set = set(my_str)
#     my_set_1 = set(my_str_1)
#     for symbol in my_set.intersection(my_set_1):
#         if my_str_1.lower().count(symbol) == 1 and my_str.lower().count(symbol) == 1:
#             my_list.append(symbol)
#     return(my_list)
#
# my_str = "I like booo"
# my_str_1 = "I like wooo"
# my_list = []
# print(new_list_creator(my_str, my_str_1))

# 8.Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# def mail_creator(names, domains):
#     my_name = random.choice(names)
#     my_domain = random.choice(domains)
#     my_number = str(random.randint(100, 999))
#     my_str = ''.join(random.choice(string.ascii_letters.lower()) for number in range(random.randint(5,7)))
#     my_list = [my_name,".", my_number, my_str,"@", my_domain]
#     my_email = "".join(my_list)
#     return my_email
#
#
# names = ["lerchik", "zhekos", "ciri"]
# domains = ["gmail.com", "ukr.net", "mail.ru"]
# print(mail_creator(names,domains))















