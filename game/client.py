import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Подключаемся к серверу

    # Запрос выбора у клиента
    client_choice = input("Выберите камень, ножницы или бумага: ").lower()

    # Отправляем выбор сервера
    client_socket.send(client_choice.encode())

    # Получаем выбор сервера и результат
    server_choice = client_socket.recv(1024).decode()
    result = client_socket.recv(1024).decode()

    print(f"Сервер выбрал: {server_choice}")
    print(f"Результат игры: {result}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
