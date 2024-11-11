from datetime import datetime

def calculateAge():
    while True:
        # Запрашиваем дату рождения пользователя
        birthDateStr = input("Введите дату рождения (день/месяц/год): ")
        
        # Преобразуем введённую строку в объект datetime
        try:
            birthDate = datetime.strptime(birthDateStr, "%d/%m/%Y")
            break  # Если дата введена корректно, выходим из цикла
        except ValueError:
            print("Некорректный формат даты. Используйте формат день/месяц/год.")
    
    # Получаем текущую дату
    today = datetime.today()
    
    # Проверка на то, что дата рождения меньше сегодняшней
    if birthDate >= today:
        print("Ошибка: дата рождения не может быть позже или равна сегодняшнему дню.")
        return
    
    # Рассчитываем возраст
    age = today.year - birthDate.year
    
    # Учитываем, был ли день рождения в этом году
    if (today.month, today.day) < (birthDate.month, birthDate.day):
        age -= 1
    
    print(f"Ваш возраст: {age} лет")

# Вызов функции
calculateAge()
