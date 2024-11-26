import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо AsyncPath для асинхронної роботи з файловими шляхами
from aiopath import AsyncPath

# Основна асинхронна функція


async def main():
    """
    Виконує асинхронні перевірки властивостей файлу або директорії,
    використовуючи AsyncPath.
    """
    # Створюємо об'єкт AsyncPath для роботи з файлом "hello.txt"
    apath = AsyncPath("hello.txt")

    # Перевіряємо, чи існує файл або директорія
    print(await apath.exists())  # Повертає True, якщо шлях існує, інакше False

    # Перевіряємо, чи є шлях файлом
    # Повертає True, якщо шлях є файлом, інакше False
    print(await apath.is_file())

    # Перевіряємо, чи є шлях директорією
    # Повертає True, якщо шлях є директорією, інакше False
    print(await apath.is_dir())

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    asyncio.run(main())  # Запускаємо асинхронну функцію
