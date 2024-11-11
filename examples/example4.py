#Пример получения/разбиения аргументов – ключевых слов с помощью символа *:
def example4(*args):
    print('Positional argument tuple:', args)
example4()
example4(5, 212312, 444444, 'argument')