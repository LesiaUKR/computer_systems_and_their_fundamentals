import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням

# Асинхронна функція, яка симулює довготривалу задачу


async def long_running_task():
    """
    Симулює довготривалу задачу з можливістю її скасування.
    """
    try:
        # Імітуємо довготривалу операцію (затримка на 10 секунд)
        await asyncio.sleep(10)
        return "Завдання завершено"  # Якщо задача не скасована, повертаємо результат
    except asyncio.CancelledError:  # Обробляємо скасування задачі
        # Виводимо повідомлення, що задача скасована
        print("Завдання було скасовано")
        raise  # Повторно піднімаємо виняток, щоб він був оброблений у головній програмі

# Основна асинхронна функція


async def main():
    """
    Створює довготривалу задачу, чекає деякий час і скасовує її.
    """
    task = asyncio.create_task(
        long_running_task())  # Створюємо і запускаємо асинхронну задачу

    await asyncio.sleep(1)  # Чекаємо 1 секунду перед тим, як скасувати задачу
    task.cancel()  # Скасовуємо задачу

    try:
        await task  # Очікуємо завершення задачі (або обробляємо її скасування)
    except asyncio.CancelledError:  # Обробляємо скасування задачі в головній програмі
        # Повідомлення про скасування
        print("Головна програма: Завдання скасовано")

# Основний блок виконання
if __name__ == "__main__":
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    asyncio.run(main())  # Запускаємо основну функцію