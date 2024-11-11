#Пример использования лямбда функции
#Реализация примера без лямбад функции
def book_list(books, func):
    for book in books:
        print(func(book))
books = ['Бойцовский клуб','Граф Монте Кристо','Сталкер']
def book_print(book):
    return book.upper() + ' - уже было'
book_list(books, book_print)
#Реализация примера с лямбда функцией
def book_list(books, func):
    for book in books:
        print(func(book))
books = ['Бойцовский клуб','Граф Монте Кристо','Сталкер']
book_list(books, lambda book: book.upper() + ' - уже было')