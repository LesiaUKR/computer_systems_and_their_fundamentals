import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
import requests  # Імпортуємо requests для виконання HTTP-запитів
# Імпортуємо ThreadPoolExecutor для роботи з потоками
from concurrent.futures import ThreadPoolExecutor
from time import time  # Імпортуємо time для вимірювання часу виконання

# Список URL-адрес, з яких будемо отримувати дані
urls = ['<http://www.google.com>',
        '<http://www.python.org>', '<http://duckduckgo.com>']

# Синхронна функція для отримання попереднього перегляду вмісту веб-сторінки


def preview_fetch(url):
    """
    Виконує HTTP-запит GET до вказаного URL і повертає URL разом із першим фрагментом тексту відповіді.

    Аргументи:
        url (str): URL-адреса для запиту.

    Повертає:
        tuple: URL-адреса і перші 150 символів тексту відповіді.
    """
    r = requests.get(url)  # Виконуємо HTTP-запит GET
    # Повертаємо URL і перші 150 символів тексту відповіді
    return url, r.text[:150]

# Асинхронна функція для асинхронного виконання preview_fetch


async def preview_fetch_async():
    """
    Виконує preview_fetch для кожного URL у списку urls за допомогою ThreadPoolExecutor.

    Повертає:
        list[tuple]: Список результатів (URL і попередній перегляд вмісту).
    """
    # Отримуємо поточний подієвий цикл
    loop = asyncio.get_running_loop()

    # Створюємо ThreadPoolExecutor із трьома потоками
    with ThreadPoolExecutor(3) as pool:
        # Запускаємо preview_fetch у потоках для кожного URL
        futures = [loop.run_in_executor(
            pool, preview_fetch, url) for url in urls]

        # Чекаємо завершення всіх завдань за допомогою asyncio.gather
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result  # Повертаємо результати виконання

# Основний блок виконання
if __name__ == '__main__':
    """
    Вимірює час виконання preview_fetch_async і виводить результати.
    """
    start = time()  # Записуємо час початку виконання

    # Виконуємо асинхронну функцію preview_fetch_async
    r = asyncio.run(preview_fetch_async())

    # Виводимо результати виконання
    print(r)

    # Виводимо загальний час виконання
    print(time() - start)
