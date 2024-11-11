#Функция - генератор которая генерирует числа в заданном диапазоне
def get_number():
    for i in range(1,30,2):
        yield i
#Счетчик индекса, переменная для хранения последнего числа
counter = 0
last = 0
#Цикл for для вывода переменных с заданными индексами
for i in get_number():
    counter+=1
    if counter == 1:
        print(i)
    elif counter == 5:
        print(i)
    last = i
print(last)