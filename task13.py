# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# 1 вариант:
stroka1 = input("Введите малую строку: ")
stroka2 = input("Введите большую строку: ")

print(f"1: первая строка входит во вторую {stroka2.count(stroka1)} раз.")

# 2 вариант:
count = 0
i = 0
while i <= len(stroka2):
    if stroka1 in stroka2[i: i+len(stroka1)]: # это срез stroka[:]
        count = count + 1                     #print("Найдено повторение номер", count+1)
        i = i + len(stroka1)
    else:
        i = i + 1

print(f"2: первая строка входит во вторую {count} раз(а).")






# 3 вариант:
# stroka1 = set(stroka1)
# stroka2 = set(stroka2)
# print(type(stroka1))
# print(type(stroka2))
# result = stroka2.intersection(stroka1)
# print(type(result))
# print(f"3: первая строка входит во вторую {result} раз.")

