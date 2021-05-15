import os
from os import path
import json

# with open("lesson2.py", "r") as txt_file:
#     data = txt_file.readlines()
# # data = data.split("\n")
# print(data)
# data.append("# test \n#TEST\n")

# data = ["jhfggkhfh", "dghfdgf", "gfdhfd"]
#
# with open("lesson2_test.py", "w") as txt_file:
#     txt_file.write("\n".join(data))
#
# def list_writer(filename, data):
#     with open(filename, "w") as txt_file:
#         txt_file.write(str(data))
# def list_reader(filename):
#     with open(filename, "r") as json_file:
#         data = txt_file.read()
#     return data
# filename = "tmp/test.txt"
# data = [1, 2, 3, 4, 5]
# data_new = list_reader(filename)
# print(data_new)
#
# list_writer(filename, data)




# source_dir = os.getcwd()
# files = os.listdir(source_dir)
# files = sorted(files)
# print(files)
# total_files = []
# for filename in files:
#     if os.path.isfile(os.path.join(source_dir, filename)):
#         total_files.append(filename)
# print(total_files)


# current_dir = os.getcwd()
# print(current_dir)

# new_dir = os.path.join(source_dir, "tmp")
# print(new_dir)
# files = os.listdir(new_dir)
# print(files)

# try:
#     os.mkdir("tmp")
# except FileExistsError:
#     pass

# os.makedirs("tmp_3", exist_ok=True)

import os
import string

def create_dir(dirname):
    os.makedirs(dirname, exist_ok=True)

def create_alphabet_files(dirname):
    alphabet = string.ascii_lowercase
    for symbol in alphabet:
        create_file(dirname, symbol, alphabet)

def create_file(symbol, alphabet):
    filename = os.path.join(dirname, f"{symbol}".txt)
    with open(filename, "w") as file:
        file.write(alphabet.replace(symbol, symbol.upper()))



dirname = "alphabet"
create_dir(dirname)
create_alphabet_files(dirname)