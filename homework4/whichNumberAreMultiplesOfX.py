import random

def findMultiples():
    # Генерация списка случайных чисел от 0 до 200, размер списка - 10
    numbers = [random.randint(0, 200) for _ in range(random.randint(10,50))]
    
    # Запрос цифры X с клавиатуры
    while True:
        x = input("Введите цифру от 1 до 9: ")
        if x.isdigit() and 1 <= int(x) <= 9:
            x = int(x)
            break
        else:
            print("Ошибка! Введите цифру от 1 до 9.")

    # Используем лямбда-функцию для фильтрации чисел, кратных X
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    # Выводим все найденные числа, кратные X
    print(f"Сгенерированные числа: {numbers}")
    print(f"Числа, кратные {x}: {multiples}")

# Вызов функции
findMultiples()
