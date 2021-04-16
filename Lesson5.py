# from random import randint
# main_value = randint(1, 10)
# count = 5
# while go_game and count:
# count -= 1

# if value.isdigit():
#     value = int(value)

# try: block_coda
# except ValueError:
#     pass

# ord_value = ord("A")
# print(ord_value)
# chr_value = chr(98)
# print(chr_value)

# my_list = [12, 34, 5, 1, -6, 100]
# my_list.sort()
# print(my_list)
# new_list = sorted(my_list, reverse=True)
# print(my_list)
# print(new_list)
# print(max(my_list))
# print(sum(my_list))

# my_list = list("qwertyFGH []&")
# new_list = sorted(my_list)
# print(new_list)

# my_str = "blablacar"
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# symbol_list = [my_symbol] * count
# for line in symbol_list:
#     print(line)
#
# for _ in range(count):
#     print(my_symbol)

# my_str = "bla BLA car"
# result_str = ""
# for symbol in my_str.upper():
#     if symbol not in result_str:
#         result_str += symbol
# print(len(result_str))

# my_str = "bla BLA car"
# result_str = []
# for symbol in my_str.upper():
#     if symbol not in result_str:
#         result_str.append(symbol)
# print(len(result_str))

# my_str = "assdhjksgjkfdbgfjkryuitbvdsjm"
# my_list = []
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)
def run_task_with_enumerated_list(hello_from):
    print("Hello from run_task_with_enumerated_list " + hello_from)
    my_list = []
    my_str = "qwerty"
    str_index = [1, 4, 3, 3, 2, 0, 5, 5, 1, 0, 0, 3]
    for idx, value in enumerate(str_index):
        my_list.append(value)

    print(my_list)


# my_number = 12324398764893762890798640946562543984689439705191301597489
# count = len(str(my_number))
# print(count)

# max_digit = max(str(my_number))
# print(max_digit)

# new_value =int(str(my_number)[::-1])
# print(new_value)


run_task_with_enumerated_list("Lera")
run_task_with_enumerated_list("Zhenya")
run_task_with_enumerated_list("Denis")
