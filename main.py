
str_l = [] #список для первых букв
string = input("Введите строку : ") # Ввод строки 
words = string.split()
for word in words:# Извлекаем первые буквы каждого слова
 str_l.append(word[0])  # Добавляем первую букву слова в новый список

result = ''.join(str_l) # Список первых букв переводим в строку
print("Строка из первых букв: ", result)