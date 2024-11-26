from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import requests

# Функція для отримання тексту з URL


def get_text(url):
    try:
        # Виконуємо GET-запит до URL
        response = requests.get(url)
        # Перевіряємо наявність помилок HTTP
        response.raise_for_status()
        # Повертаємо текст відповіді
        return response.text
    except requests.RequestException as e:
        # У разі помилки повертаємо None
        print(f"Помилка при отриманні тексту: {e}")
        return None

# Функція Map: перетворює слово у пару (слово, 1)


def map_function(word):
    return word, 1

# Функція Shuffle: групує значення за ключами (слова)


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

# Функція Reduce: підраховує загальну кількість кожного слова


def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

# Виконання MapReduce


def map_reduce(text):
    # Розбиваємо текст на окремі слова
    words = text.split()
    print(f"Кількість слів у тексті: {len(words)}")  # Вивід кількості слів

    # Паралельний Маппінг
    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))
    # Виводимо перші 10 результатів
    print(f"Приклад результатів маппінгу: {mapped_values[:10]}")

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)
    print(f"Приклад результатів shuffle: {
          list(shuffled_values)[:10]}")  # Виводимо перші 10 пар

    # Паралельна Редукція
    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))
    # Виводимо перші 10 результатів
    print(f"Приклад результатів редукції: {reduced_values[:10]}")

    # Повертаємо кінцевий результат у вигляді словника
    return dict(reduced_values)


if __name__ == "__main__":
    # URL для отримання тексту
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    if text:
        # Виконання MapReduce на вхідному тексті
        result = map_reduce(text)
        # Виводимо перші 10 слів та їх кількість
        print("Результат підрахунку слів:", list(result.items())[:10])
    else:
        print("Помилка: Не вдалося отримати вхідний текст.")
