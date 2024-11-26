import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо AsyncPath для асинхронної роботи з файловими шляхами
from aiopath import AsyncPath
# Імпортуємо асинхронну функцію copyfile для копіювання файлів
from aioshutil import copyfile

# Основна асинхронна функція


async def main():
    """
    Асинхронно перевіряє існування файлу "hello.txt",
    створює директорію "logs" (якщо вона не існує),
    і копіює файл "hello.txt" до цієї директорії.
    """
    # Створюємо об'єкт AsyncPath для файлу "hello.txt"
    apath = AsyncPath("hello.txt")

    # Перевіряємо, чи існує файл "hello.txt"
    if await apath.exists():
        # Створюємо об'єкт AsyncPath для директорії "logs"
        new_path = AsyncPath("logs")

        # Створюємо директорію "logs", якщо вона ще не існує
        await new_path.mkdir(exist_ok=True, parents=True)

        # Копіюємо файл "hello.txt" у директорію "logs"
        # нове ім'я файлу буде таким самим, як оригінал
        await copyfile(apath, new_path / apath)

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    asyncio.run(main())  # Запускаємо асинхронну функцію
