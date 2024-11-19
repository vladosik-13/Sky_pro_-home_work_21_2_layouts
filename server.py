from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

# Определяем путь к файлу contacts.html относительно текущего скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'contacts.html')

class MyServer(BaseHTTPRequestHandler):
    """ Специальный класс, который отвечает за обработку входящих запросов от клиентов"""
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
