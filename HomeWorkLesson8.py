# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# people_list = [{"name": "John", "age": 15}, {"name": "Bradley", "age": 15},{"name": "Jack", "age": 45}]
# from collections import defaultdict
#
# people_list = [{"name": "John", "age": 15},
#                {"name": "Bradley", "age": 15},
#                {"name": "Jack", "age": 45}]
#
# age_by_names = defaultdict(list)
# len_name_by_names = defaultdict(list)
# ages = []
#
# for people in people_list:
#     name = people["name"]
#     age = people["age"]
#     age_by_names[age].append(name)
#     len_name_by_names[len(name)].append(name)
#     ages.append(age)
#
# min_age = min(age_by_names)
# print("min_age:", *age_by_names[min_age])
#
# max_len_name = max(len_name_by_names)
# print("max_len_name:", *len_name_by_names[max_len_name])
#
# print("average:", sum(ages) // len(ages))

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
my_dict_1 = {"a":1, "b":2, "c":3}
my_dict_2 = {"a":11, "bb":22, "cc":33}
# a)
# result = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(result)
# б)
# result = list((set(my_dict_1.keys())).difference(set(my_dict_2.keys())))
# print(result)
# в)
# result = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
# print(result)
# г)
result = {}
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        result[item[0]] = item[1]
    else:
        result[item[0]] = [item[1], my_dict_2[item[0]]]

print(result)



