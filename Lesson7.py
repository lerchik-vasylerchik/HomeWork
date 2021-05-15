my_list_1 = [1,3,5]
my_list_2 = [20,30,40]
my_result = []

for index in range(len(my_list_1)):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
print(my_result)

my_list_1 = [1,3,5,7]
my_list_2 = [20,30,40]
my_result = []

range_len = min(len(my_list_1), len(my_list_2))
for index in range(range_len):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
if len(my_list_1)> len(my_list_2):
    tail_list = my_list_1[range_len:]
else:
    tail_list = my_list_2[range_len:]
my_result +=tail_list
print(my_result)

# my_list = list(range(100))
# print(my_list)

# my_list = []
# for number in range(15):
#     my_list.append(number**2)
# print(my_list)

# my_list_gen = [number**2 for number in range(15)]
# print(my_list_gen)
# str_list = [str(value) for value in my_list_gen]
# result_number = int(''.join(str_list))
# print(result_number)

# alphabet_list = [chr(index) for index in range(ord("A"), ord("Z")+1)]
# print(alphabet_list)

# my_list = ["qwe", "asd", "123", 234, 45]
# new_list = [value * 2 for value in my_list if type(value) == str]
# print(new_list)
# my_list = ["/home/dn233333333/PycharmProjects/Hillel/", "/home/dn233333333/PycharmProjects/Pandas/", "/home/dn233333333/PycharmProjects/Pandas/"]
# [print(path) for path in my_list]

# my_set = set(my_list)
# print(my_set, type(my_set))

# my_path = "/home/dn233333333/PycharmProjects/Hillel/"
#
# my_path_set = set(my_path)
# print(len(set(my_path)), my_path_set)
# my_path_p = "/home/dn233333333/PycharmProjects/Pandas@/"
# my_path_s = "/home/dn233333333/PycharmProjects/Hillel#/"
# my_path_p_set = set(my_path_p)
# my_path_s_set = set(my_path_s)
# path_union_set = my_path_p_set.union(my_path_s_set)
# my_path_s_set.update(my_path_p_set)
# print(my_path_s_set)
# path_union_set = my_path_p_set | my_path_s_set
# print(path_union_set)

# my_path_p = "/home/dn233333333/PycharmProjects/Pandas@/"
# my_path_s = "/home/dn233333333/PycharmProjects/Hillel#/"
# my_path_p_set = set(my_path_p)
# my_path_s_set = set(my_path_s)
# path_union_set = my_path_p_set & my_path_s_set
# print(path_union_set)

# my_path_p = "/home/dn233333333/PycharmProjects/Pandas@/"
# my_path_s = "/home/dn233333333/PycharmProjects/Hillel#/"
# my_path_p_set = set(my_path_p)
# my_path_s_set = set(my_path_s)
# path_difference_set = my_path_p_set.difference(my_path_s_set)
# print(path_difference_set)

# my_list = ["qwe", "rt", "g", "g", "g", "g"]
# for line in set(my_list):
#     count = my_list.count(line)
#     print(line, count)

# person = {"name": "John",
#           "age":23,
#           "job":["cop", "doctor"],
#           "address": {"city":"Dnipro",
#                       "street":"Polya"}}
# print(person["name"])

# key = "NEW"
# value = [1, 2, 3]
# dummy = {key:value}
# print(dummy)
# dummy["New"] = "Hello"
# print(dummy["new"])