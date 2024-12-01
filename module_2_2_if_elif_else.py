# name = input("Введите ваше имя: ")
# if name == "Irina": # Условие, ветвление
#     print("Здравствуйте госпожа ", name)
# print("Здравствуйте ", name)

# print("-----------Пример с блоком else-----------------")
#
# name = input("Введите ваше имя: ")
# if name == "Irina": # Условие, ветвление
#     print("Здравствуйте госпожа", name)
# else:
#     print("Здравствуйте", name, "Отработал блок else")

# print("-----------Пример с блоком elife-----------------")
# # Оператор and строго проверяет соблюдения всех условий. Оператор or ему достаточно если хотя бы ОДНО из условий верно
# number = int(input("Введите число: "))
# if number % 3 == 0 and number % 5 == 0:
#     print(f"{number} делится на 3 и на 5 без остатка")
# elif number % 3 == 0:
#     print(f"{number} делится на 3 без остатка")
# elif number % 5 == 0:
#     print(f"{number} делится на 5 без остатка")
# else:
#     print(f"{number} Число не делится ни на 3 ни на 5 без остатка")

# print("Введите три числа для сравнения.")
# first = int(input("Введите какое либо число для сравнения №1: "))
# second = int(input("Введите какое либо число для сравнения №2: "))
# third = int(input("Введите какое либо число для сравнения №3: "))
# if first == second == third:
#     print("Все числа равны")
# elif first == second or first == third or second == third:
#     print("Два числа равны")
# else:
#     print("Все числа разные")

while True: # Применил цикл While из следующей темы!!! Это же бомба.
    print("Введите три числа для сравнения.")
    first = int(input("Введите какое либо число для сравнения №1: "))
    second = int(input("Введите какое либо число для сравнения №2: "))
    third = int(input("Введите какое либо число для сравнения №3: "))
    if first == second == third:
        print("Все числа равны")
    elif first == second or first == third or second == third:
        print("Два числа равны")
        continue
    else:
        print("Все числа разные")
        break