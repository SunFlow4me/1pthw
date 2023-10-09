def print_two(*args): #def создаёт множество функций(* даёт возможность вводить множество значений)
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2): #def создаёт две функции
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1): #def создаёт функцию
    print(f"arg1: {arg1}")

def print_none(): #def создаёт и присваивает имя ничему
    print("здесь ничего нет")

print_two("Виталий","Цаль") #присваивание имени
print_two_again("Виталий","Цаль")
print_one("Первый")
print_none()