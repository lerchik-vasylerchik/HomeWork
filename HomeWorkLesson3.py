value = 120
new_value = value/2 if value < 100  else - value
print(new_value)
########################################################################################################################
value = 28
new_value= 1 if value < 100 else 0
print(new_value)
########################################################################################################################
value = 45
new_value= True if value < 100 else False
print(new_value)
########################################################################################################################
my_str = "real_hazker"
print (my_str [1::2])
########################################################################################################################
my_str = "real_hazker"
print (my_str [::2])
########################################################################################################################
my_str = "real_hazker"
new_str = my_str*2 if len(my_str) < 5 else my_str
print(new_str)
########################################################################################################################
my_str = "real_hazker"
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)
########################################################################################################################

value = input("Угадай мое число:")
value_letter = True
while value_letter:
    if value.isalpha():
        number = str(value)
        value = input("Число!!!!!!!!!:")

    if value.isdigit ():
        number = int(value)
        wrong_number= True
        value_letter = False

wrong_number = True
while wrong_number:
    value_letter = False

    if number == 7:
        value_1 = "Успех!"
        str(value)
        print(value_1)
        wrong_number = False

    elif number > 7:
        value_2 = input("Введи число поменьше:")
        number = int(value_2)
    elif number < 7:
        value_3 = input("Введи число побольше:")
        number = int(value_3)






