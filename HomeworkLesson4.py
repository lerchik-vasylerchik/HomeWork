# my_list = [1, 9000, 7000, 5, 6, 80]
# for value in my_list:
#     if value > 100:
#         print(value)
# ########################################################################################################################
# my_list = [1, 9000, 7000, 5, 6, 80]
# result = []
# for value in my_list:
#     if value > 100:
#         result.append(value)
# print(result)
########################################################################################################################
# my_list = [1, 9000, 7000, 5, 6, 80]
# if len(my_list) < 2:
#     my_list.append(0)
#     print(my_list)
# elif len(my_list) >= 2:
#     my_list.append(my_list[-1] + my_list[-2])
#     print(my_list)
########################################################################################################################
my_string = '0123456789'
my_string_2 = '0123456789'
new_list = []
# new_list.append(my_string)
for symb_1 in my_string:
    for symb_2 in my_string_2:
        my_string = (int(symb_1 + symb_2))
        # new_list = []
        new_list.append(my_string)
print(str(new_list))
