# 38. Напишите программу, удаляющую из текста все слова содержащие "абв"

text = '38. Напишите ываабв программу, абвцукв удаляющую абвкеке из текста алоабвабвин все слова содержащие "абв" '
print('Исходный список', text)
spisok_slov = text.split(' ') # разделяем строку на слова

# 1 ВАРИАНТ 
spisok_slov2 = list(filter(lambda x: 'абв' not in x, spisok_slov)) # фильбром удаляем слова содержащие 'абв'
text1 = " ".join(spisok_slov2) # слепляем слова обратно в строку с разделителем пробелом
print('Отредактированный список1: ', text1)


# 2 ВАРИАНТ
spisok_slov4 = []
for i in spisok_slov:
    if 'абв' not in i:
            spisok_slov4.append(i) # создаём новый список без слов содержащих 'абв'
text2 = ' '.join(spisok_slov4)   # слепляем слова обратно в строку с разделителем пробелом
print('Отредактированный список2:', text2)

# 3 ВАРИАНТ
spisok_slov6 = []
for i in spisok_slov:
    if i.find('абв') == -1:
            spisok_slov6.append(i) # создаём новый список без слов содержащих 'абв'
text3 = ' '.join(spisok_slov6)   # слепляем слова обратно в строку с разделителем пробелом
print('Отредактированный список3:', text3)
