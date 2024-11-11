#Функция с одним аргументом
def example2(time):
    if time=="night":
        return "I cant see"
    elif time =="day":
        return "I can see great"
    else:
        return "Vision is 50/50"
vision = example2("night")
print(vision)       