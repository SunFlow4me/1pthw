from sys import argv

script, filename = argv

print("очистка файл")
print("чтобы продолжить нажмите enter")

input("?")

print("открытие...")
target = open(filename, "w")

print("очистка...")
target.truncate()

print("Введите 3 новые строчки")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("запись...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("закрываю...")
target.close()