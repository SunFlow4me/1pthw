from sys import argv
from os.path import exists

script, from_file, to_file = argv #третьим аргументом надо ввести название третьего файла который не существует в примере, но я создал его

print(f"копирование из {from_file} в {to_file}")

in_file = open(from_file)
indata = in_file.read()

print("Для продолжения нажмите Enter, для отмены CTRL+C") #у меня при использовании ctrl+c просто вылезает ошибка и программа останавливается, видемо так и задуманно
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("закончили")

out_file.close()
in_file.close()