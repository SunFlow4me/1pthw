from sys import argv

script, file = argv

def print_all(f):
    print(f.read())#"f" указатель, который ориентируется при выводе строк

def rewind(f):
    f.seek(0) #.seek указывает позицию для указателя чтения/записи, (0) обозначает начало файла, без этого строчки 22-30 ничего не будут выводить

def print_a_line(line_count, f):
    print(line_count, f.readline())#выбор строки и её чтение

current_file = open(file)

print("Первым делом выводим\n")
print_all(current_file)

print("отмотаем назад")
rewind(current_file)

print("Выведем три строчки")
current_line = 1 #присваивание числа/номера строки
print_a_line(current_line, current_file)#присваивание номера этой строки для line_count и чтения её в файле

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)