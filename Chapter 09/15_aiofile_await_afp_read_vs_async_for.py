# Імпортуємо async_open з aiofile для асинхронної роботи з файлами
import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо async_open з aiofile для асинхронної роботи з файлами
from aiofile import async_open

# Основна асинхронна функція


async def main():
    """
    Відкриває файл "hello.txt" для читання і виводить його вміст на екран.
    """
    # Використовуємо async_open для відкриття файлу у режимі "r" (читання)
    async with async_open("hello.txt", "r") as afp:
        # Читаємо вміст файлу асинхронно і виводимо його на екран
        print(await afp.read())

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """


# ПРИКЛАД З async for

# async def main():
#     """
#     Асинхронно відкриває файл "hello.txt" у режимі читання,
#     читає його пострічно і виводить кожен рядок на екран.
#     """
#     # Використовуємо async_open для відкриття файлу у режимі "r" (читання)
#     async with async_open("hello.txt", 'r') as afp:
#         # Асинхронно ітеруємося по рядках файлу
#         async for line in afp:
#             print(line)  # Виводимо кожен рядок на екран

# # Основний блок виконання
# if __name__ == '__main__':
#     """
#     Запускає основну асинхронну функцію main за допомогою asyncio.run.
#     """
#     asyncio.run(main())  # Запускаємо асинхронну функцію
