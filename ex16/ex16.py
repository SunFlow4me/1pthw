from sys import argv

script, filename = argv

print("очистка файла")
print("чтобы продолжить нажмите enter")

input("?")

print("открытие...")
target = open(filename, 'w') # 'w' это строка, которая открывает файл в режиме записи(w = write, также можно открывать файлы в режиме чтения 'r' = read и тд)

print("очистка...")
target.truncate() #.truncate полностью очищает файл

print("Введите 3 новые строчки")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("запись...")

target.write(line1) #.write записывает данные
target.write("\n") #\n это управляющая последовательность, она делает отступ. без неё все введённые данные были бы в одной строке
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("закрываю...")
target.close()#.close закрытие файла