import socket

def determine_winner(player1_choice, player2_choice):
    """Определяет победителя по правилам Камень, Ножницы, Бумага."""
    if player1_choice == player2_choice:
        return "Ничья!"
    elif (player1_choice == "камень" and player2_choice == "ножницы") or \
         (player1_choice == "ножницы" and player2_choice == "бумага") or \
         (player1_choice == "бумага" and player2_choice == "камень"):
        return "Клиент победил!"
    else:
        return "Клиент проиграл!"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Ожидаем подключения на порту 12345
    server_socket.listen(1)  # Ожидаем одно подключение
    print("Сервер запущен. Ожидаем подключения...")

    client_socket, client_address = server_socket.accept()
    print(f"Подключение с {client_address} установлено.")

    # Получаем выбор клиента
    client_choice = client_socket.recv(1024).decode()

    # Запрос выбора для сервера
    server_choice = input("Выберите камень, ножницы или бумага: ").lower()

    # Определяем победителя
    result = determine_winner(client_choice, server_choice)
    print(f"Клиент выбрал: {client_choice}")
    print(f"Результат: {result}")

    # Отправляем выбор сервера и результат обратно клиенту
    client_socket.send(server_choice.encode())
    client_socket.send(result.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
