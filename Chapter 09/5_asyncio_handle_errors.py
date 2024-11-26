import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням

# Асинхронна функція, яка симулює помилкове завдання


async def faulty_task():
    """
    Ця функція навмисно викликає ValueError для демонстрації
    обробки винятків в асинхронних задачах.
    """
    raise ValueError(
        "Помилка у завданні")  # Викликає ValueError із повідомленням

# Основна асинхронна функція


async def main():
    """
    Основна функція, яка створює асинхронну задачу та обробляє винятки, якщо вони виникають.
    """
    task = asyncio.create_task(
        faulty_task())  # Створюємо і запускаємо асинхронну задачу

    try:
        await task  # Чекаємо завершення виконання завдання
    except ValueError as e:  # Обробляємо виняток ValueError, якщо він виникне
        # Виводимо повідомлення про виняток
        print(f"Виняток під час виконання завдання: {e}")
    else:
        # Якщо задача завершилася успішно, отримуємо результат
        print(f"Завдання завершилося успішно: {task.result()}")

# Основний блок виконання
if __name__ == '__main__':
    """
    Запускаємо основну асинхронну функцію `main` за допомогою asyncio.run.
    """
    asyncio.run(main())
