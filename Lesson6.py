# my_list = ['qw','sd','rty','tyu']
# result = []
# for value in my_list:
#     new_value = value.upper()
#     result.append(new_value)
# print(result)
# for index in range(len(my_list)):
#     value = my_list[index]
#     if not index % 2:
#         new_value = value.upper()
#     else:
#         new_value = value
#     result.append(new_value)
# print(result)

my_list = ['qw','sd','rty','tyu']
result = []

# for index in range(len(my_list)):
#     value = my_list[index]
#     if not index % 2:
#         value = value.upper()
#     result.append(value)
# print(result)

# for index in range(len(my_list)):
#     value = my_list[index]
#     if len(value) == 2:
#        continue
#     value = value.upper()
#     result.append(value)
# print(result)

# for index, value in enumerate(my_list):
#     if not index % 2:
#         value = value.upper()
#     result.append(value)
# print(result)

some_string = "My name is Vova. I`m 41. But I still believe in magic. Expelliarmus!"
# result = []
# for symbol in some_string:
#     if symbol.isupper():
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# result = []
# for symbol in some_string:
#     if symbol.islower():
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# result = []
# for symbol in some_string:
#     if symbol.isupper() and symbol.lower() in "eyuioa":
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# result = []
# for symbol in some_string:
#     if symbol.islower() and symbol.lower() not in "eyuioa":
#         result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# result = []
# for symbol in some_string:
#     if symbol.islower():
#         symbol = symbol.upper()
#     elif symbol.isupper():
#         symbol = symbol.lower()
#     result.append(symbol)
# result_str = "".join(result)
# print(result_str)

# big_letter = []
# small_a = []
# small_b = []
# symbols = []
# result = []
# for symbol in some_string:
#     if symbol.isupper():
#         big_letter.append(symbol)
#     elif symbol in "eyuioa":
#         small_a.append(symbol)
#     elif symbol.isalpha():
#         small_b.append(symbol)
#     else:
#         symbols.append(symbol)
# result = sorted(big_letter) + sorted(small_a) + symbols
# result_str = "".join(result)
# print(result_str)











