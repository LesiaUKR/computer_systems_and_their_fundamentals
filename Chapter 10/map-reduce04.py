import string
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
import requests

# Функція для отримання тексту з URL


def get_text(url):
    try:
        # Виконуємо GET-запит до URL
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на наявність помилок HTTP
        return response.text
    except requests.RequestException as e:
        # У разі помилки повертаємо None
        print(f"Помилка при отриманні тексту: {e}")
        return None

# Функція для видалення знаків пунктуації


def remove_punctuation(text):
    # Використовуємо метод translate для видалення пунктуації
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    print("Перші 200 символів після видалення пунктуації:",
          cleaned_text[:200])  # Вивід очищеного тексту
    return cleaned_text

# Функція Map: перетворює слово у пару (слово, 1)


def map_function(word):
    return word, 1

# Функція Shuffle: групує значення за ключами (слова)


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    # Вивід перших 10 результатів shuffle
    print("Приклад результатів shuffle:", list(shuffled.items())[:10])
    return shuffled.items()

# Функція Reduce: підраховує загальну кількість кожного слова


def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

# Основна функція для виконання MapReduce


def map_reduce(text, search_words=None):
    # Видалення знаків пунктуації
    text = remove_punctuation(text)

    # Розбиття тексту на слова
    words = text.split()
    print(f"Кількість слів у тексті: {len(words)}")  # Вивід кількості слів

    # Якщо задано список слів для пошуку, враховувати тільки ці слова
    if search_words:
        words = [word for word in words if word.lower() in search_words]
        # Вивід кількості слів після фільтрації
        print(f"Кількість слів після фільтрації: {len(words)}")

    # Паралельний Маппінг
    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))
    # Вивід перших 10 результатів маппінгу
    print(f"Приклад результатів маппінгу: {mapped_values[:10]}")

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Паралельна Редукція
    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))
    # Вивід перших 10 результатів редукції
    print(f"Приклад результатів редукції: {reduced_values[:10]}")

    # Повертаємо кінцевий результат у вигляді словника
    return dict(reduced_values)


if __name__ == "__main__":
    # URL для отримання тексту
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    if text:
        # Виконання MapReduce на вхідному тексті
        search_words = ["war", "peace", "love"]  # Слова для пошуку
        result = map_reduce(text, search_words)

        # Виведення результатів
        print("Результат підрахунку слів:", result)
    else:
        print("Помилка: Не вдалося отримати вхідний текст.")
