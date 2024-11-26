import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо AIOFile для роботи з файлами та LineReader для пострічного читання
from aiofile import AIOFile, LineReader

# Основна асинхронна функція


async def main():
    """
    Асинхронно відкриває файл "hello.txt" у режимі читання,
    читає його пострічно за допомогою LineReader і виводить кожен рядок.
    """
    # Використовуємо AIOFile для асинхронного відкриття файлу у режимі "r" (читання)
    async with AIOFile("hello.txt", "r") as afp:
        # Використовуємо LineReader для пострічного читання файлу
        async for line in LineReader(afp):
            print(line)  # Виводимо кожен прочитаний рядок

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    asyncio.run(main())  # Запускаємо асинхронну функцію
