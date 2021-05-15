# standart_dict = {'dict': 1, 'dictionary':2}
# by_type_dict = dict(short = 'dict', long = 'dictionary')
# print(by_type_dict)

# list_keys = list("qwerty")
# list_values = list("123456")

# list_keys = ["qw", "asd", "fds"]
# list_values = [1,2,3,4,5,6,7]
# by_zip_dict = dict(zip(list_keys, list_values))
# print(by_zip_dict)

# list_keys = ['a', 'b']
# result = {key:100 for key in list_keys}
# print(result)

ascii_table = {chr(numb): numb for numb in range(ord("a"), ord("z") + 1)}
print(ascii_table)
# tmp_val = 100 in ascii_table
# print(tmp_val)
#
# for key in ascii_table:
#     print(key, ascii_table[key])

# new_dict = ascii_table
# new_dict["test"] = "test"
# print(ascii_table)

# key = 100
# value = ascii_table.get(key, "")
# print(value)

# for key, value in ascii_table.items():
#     print(key, value)

# keys = ascii_table.keys()
# print(keys)

# dict_1 = {1:1, 2:2, 3:3}
# dict_2 = {1:1, 22:22, 3:3}
# result = list(set(dict_1.keys()).intersection(set(dict_2.keys())))
# print(result)

# dict_1 = {1:14, 2:24, 3:3}
# dict_2 = {1:1, 22:22, 3:3}
# result = list(set(dict_1.values()).intersection(set(dict_2.values())))
# print(result)

# dict_1 = {1:14, 2:24, 3:3}
# new_dict = {value: key for key, value in dict_1.items()}
# print(new_dict)

# dict_1 = {1:14, 2:24, 3:3}
# dict_2 = {1:1, 22:22, 3:3}
# dict_1.update(dict_2)
# print(dict_1)

# total_dict = {}
# total_dict.update(dict_1)
# total_dict.update(dict_2)
# print(total_dict, dict_1)

# total_dict = {**dict_1, **dict_2}
# print(total_dict, dict_2)
price_list = [{"bread": 100}, {"water":10}, {"banana":200}]
# min_value_list = []
# for price in price_list:
#     min_value_list.append((list(price.values()))[0])
# min_value = min(min_value_list)
# print(min_value)
# for price in price_list:
#     if list(price.values())[0] == min_value:
#         print(list(price.keys())[0])

value_list = {}
for price in price_list:
    value_list[list(price.values())[0]] = list(price.keys())[0]
min_value = min(value_list)
print(min_value)
