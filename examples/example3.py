#Функция с несколькими аргументами (позиционные)
def car(engine, color, format):
    return {'engine': engine, 'color': color, 'format':format}
myCar = car('v8', 'white', 'sedan')
print(myCar)
#Функция с несколькими аргументами (по ключевым словам)
def car(engine, color, format):
    return {'engine': engine, 'color': color, 'format':format}
myCar = car(format='sedan', engine='v8',color='white')
print(myCar)