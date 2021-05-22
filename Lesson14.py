class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

point_A = Point(3,4)
print(point_A.x)
point_B = Point(5,-5)
print(point_B.x)

class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
    # def __str__(self):
    #     return f"name:{self.name}, age:{self.age}"
    def __repr__(self):
        return f"({self.name}, {self.age})"

person_1 = Person ("John", 23, "programmer")
print(person_1)
person_2 = Person ("Jane", 36)
print(person_2)

persons = [person_1,person_2]
print(persons)

import os
import string
import random

class AlphabetWorker:
    def __init__(self, dirname):
        self.dirname = dirname
        self.alphabet = string.ascii_lowercase
        self.create_dir()
    def create_dir(self):
        os.makedirs(self.dirname, exist_ok=True)
    def create_alphabet_files(self, dirname):

        for symbol in self.alphabet:
            self.create_file(symbol)
    def create_file(self, symbol):
        filename = os.path.join(self.dirname, f"{symbol}.txt")
        with open(filename, "w") as file:
            file.write(self.alphabet.replace(symbol, symbol.upper()))
    def do_tanos_click(self):
        files = sorted(os.listdir(self.dirname))
        random.shuffle(files)
        files = files[:len(files)//2]
        for file in files:
            



alphabet_worker = AlphabetWorker("alphabet")
alphabet_worker.create_alphabet_files()
alphabet_worker.do_tanos_click()
alphabet_worker.create_dir()
