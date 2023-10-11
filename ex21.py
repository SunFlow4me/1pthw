def add(a, b):
    print(f"СЛОЖЕНИЕ {a} + {b}") #return возвращает значение
    return a + b

def subtract(a, b):
    print(f"ВЫЧИТАНИЕ {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"УМНОЖЕНИЕ {a} * {b}")
    return a * b

def divide(a, b):
    print(f"ДЕЛЕНИЕ {a} / {b}")
    return a / b

print("некоторые вычисления\n")

age = add(20, 5)
height = subtract(400, 220)
weight = multiply(10, 8)
iq = divide(270, 3)
print(f"возраст - {age}, рост - {height}, вес - {weight}, IQ - {iq}\n")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("небольшой подсчёт - ", what)