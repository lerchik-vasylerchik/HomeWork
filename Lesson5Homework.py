# Дано целое число (int). Определить сколько нулей в этом числе
# number = 2803000
# zero_count = str(number).count("0")
# print(zero_count)
#######################################################################################################################
# Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
# number = 2803000
# zero_count = len(str(number)) - len((str(number).rstrip("0")))
# print(zero_count)
########################################################################################################################
#Даны списки my_list_1 и my_list_2.Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
# my_list_1 = ["pus", "ka", "bya", "ta", "ya"]
# my_list_2 = ["qw", "er", "ty"]
# my_result = []
# my_result = my_list_1[::2] + my_list_2[1::2]
########################################################################################################################
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
# my_list = [1,2,3,4]
# new_list = [] + my_list[::-1]
# print(new_list)
# Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
# my_list = [1,2,3,4]
# my_list.append(my_list.pop(0))
# print(my_list)
########################################################################################################################
# Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
# my_str = "43 больше чем 34 но меньше чем 56"
# my_list = my_str.split()
# my_list_1 = []
# for value in my_list:
#     if value.isdigit():
#         value = int(value)
#         my_list_1.append(value)
# print(sum(my_list_1))
# Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# l_index = my_str.find(l_limit)
# r_index = my_str.rfind(r_limit)
# sub_str = my_str[l_index + 1 : r_index]
# Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
# my_string = "qwertyu"
# if len(my_string) % 2:
#     my_string +="_"
# my_list = []
# for index in range(len(my_string) // 2):
#     index = index * 2
#     new_str = my_string[index: index + 2]
#     my_list.append(new_str)
# print(my_list)
# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# my_list = [2,4,1,5,3,9,0,7]
# res = 0
# for index in range(len(my_list)):
#     if index in [0, len(my_list) - 1]:
#         continue
#     if my_list[index] > my_list[index - 1] + my_list[index + 1]:
#         res += 1
# print(res)