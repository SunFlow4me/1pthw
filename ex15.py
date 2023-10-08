from sys import argv

script, filename = argv

txt = open(filename)

print(f"Содержимое файла {filename}:")
print(txt.read())