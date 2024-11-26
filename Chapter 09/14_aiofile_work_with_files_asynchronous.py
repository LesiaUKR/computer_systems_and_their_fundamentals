import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо async_open з aiofile для роботи з файлами асинхронно
from aiofile import async_open

# Асинхронна функція main


async def main():
    """
    Асинхронно відкриває файл "hello.txt" для запису, записує в нього текст
    і автоматично закриває файл після завершення роботи.
    """
    # Використовуємо async_open для відкриття файлу у режимі "w+" (запис і читання)
    async with async_open("hello.txt", "w+") as afp:
        # Записуємо текст у файл поетапно
        await afp.write("Hello ")  # Записуємо "Hello "
        await afp.write("world\n")  # Записуємо "world" і новий рядок
        # Записуємо ще один рядок тексту
        await afp.write("Hello from - async world!")

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    asyncio.run(main())  # Запускаємо асинхронну функцію
