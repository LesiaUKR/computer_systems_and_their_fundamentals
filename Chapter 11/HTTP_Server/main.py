# Модуль для визначення MIME-типів файлів (наприклад, text/html, image/jpeg).
import mimetypes
import pathlib  # Модуль для роботи з файловою системою.
# Модулі для створення HTTP-сервера.
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse  # Модуль для обробки URL-запитів.

import os
# Виводить поточний робочий каталог для діагностики.
print(f"Current working directory: {os.getcwd()}")

# Клас для обробки HTTP-запитів


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        """
        Метод для обробки HTTP POST-запитів.
        Використовується для отримання даних із запитів, наприклад, з форми.
        """
        data = self.rfile.read(int(self.headers['Content-Length'])
                               )  # Зчитує дані з тіла запиту.
        print(data)  # Виводить дані у байтах.
        # Декодує дані (розкодовує символи, наприклад, %20 у пробіл).
        data_parse = urllib.parse.unquote_plus(data.decode())
        print(data_parse)  # Виводить декодовані дані.
        data_dict = {key: value for key, value in [
            # Перетворює рядок у словник (ключ-значення).
            el.split('=') for el in data_parse.split('&')]}
        print(data_dict)  # Виводить словник.
        # Відправляє відповідь із кодом 302 (перенаправлення).
        self.send_response(302)
        # Вказує, куди перенаправити (у цьому випадку на головну сторінку).
        self.send_header('Location', '/')
        self.end_headers()  # Завершує формування HTTP-заголовків.

    def do_GET(self):
        """
        Метод для обробки HTTP GET-запитів.
        Використовується для завантаження сторінок або файлів.
        """
        pr_url = urllib.parse.urlparse(self.path)  # Розбирає шлях запиту.
        if pr_url.path == '/':  # Якщо запит на головну сторінку.
            self.send_html_file('index.html')  # Відправляє файл index.html.
        elif pr_url.path == '/contact':  # Якщо запит на сторінку "Контакти".
            # Відправляє файл contact.html.
            self.send_html_file('contact.html')
        else:  # Якщо запит на інший ресурс.
            # Перевіряє, чи існує файл.
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()  # Відправляє статичний файл.
            else:
                # Якщо файл не знайдено, відправляє сторінку помилки.
                self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status=200):
        """
        Відправляє HTML-файл як відповідь на запит.
        Параметри:
        - filename: ім'я файлу, який потрібно відправити.
        - status: HTTP-статус відповіді (за замовчуванням 200 - ОК).
        """
        self.send_response(status)  # Встановлює статус відповіді.
        # Встановлює MIME-тип файлу (HTML).
        self.send_header('Content-type', 'text/html')
        self.end_headers()  # Завершує формування HTTP-заголовків.
        # Відкриває файл у режимі читання байтів.
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())  # Відправляє вміст файлу клієнту.

    def send_static(self):
        """
        Відправляє статичний файл (наприклад, зображення чи CSS).
        """
        self.send_response(200)  # Встановлює статус відповіді (200 - ОК).
        mt = mimetypes.guess_type(self.path)  # Визначає MIME-тип файлу.
        if mt:  # Якщо MIME-тип знайдено.
            # Встановлює MIME-тип у заголовках.
            self.send_header("Content-type", mt[0])
        else:
            # Якщо MIME-тип не визначено, встановлює text/plain.
            self.send_header("Content-type", 'text/plain')
        self.end_headers()  # Завершує формування HTTP-заголовків.
        # Відкриває файл у режимі читання байтів.
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())  # Відправляє вміст файлу клієнту.

# Функція для запуску сервера


def run(server_class=HTTPServer, handler_class=HttpHandler):
    """
    Запускає HTTP-сервер.
    Параметри:
    - server_class: клас сервера (за замовчуванням HTTPServer).
    - handler_class: клас обробника запитів (за замовчуванням HttpHandler).
    """
    server_address = (
        # Визначає адресу сервера ('' означає всі доступні інтерфейси, порт 8002).
        '', 8002)
    http = server_class(server_address, handler_class)  # Створює сервер.
    try:
        http.serve_forever()  # Запускає сервер у нескінченному циклі.
    except KeyboardInterrupt:  # Якщо користувач натискає Ctrl+C.
        http.server_close()  # Закриває сервер.


# Запуск сервера
if __name__ == '__main__':
    run()  # Викликає функцію запуску.
