#перевод см в метры и кг в тонны, используя переменную и форматируя print

height = 188 # см
weight = 80 # кг

height_m = height / 100
weight_t = weight / 1000

print(f"рост в см = {height}, рост в метрах = {height_m}") #переменные в {} не будут форматироваться если в начале print не будет f
print(f"вес в кг = {weight}, вес в тоннах = {weight_t}")
