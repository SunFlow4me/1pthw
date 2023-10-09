from sys import argv

script, filename = argv

txt = open(filename) #txt присваиется команда open, которая открывает питону файл чтобы тот мог работать с ним

print(f"Содержимое файла {filename}:")
print(txt.read()) #.read в сочитании с txt открывает и читает всё что находиться внутри файла, и информация внутри файла выводится через print