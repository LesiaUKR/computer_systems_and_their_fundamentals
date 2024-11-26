import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
# Імпортуємо модуль для роботи з виконанням завдань у окремих потоках
import concurrent.futures
from time import time  # Імпортуємо time для вимірювання часу виконання

# Синхронна функція, яка виконує блокуючу задачу


def blocks(n):
    """
    Симулює блокуючу задачу шляхом зменшення лічильника до 0.

    Аргументи:
        n (int): Початкове значення лічильника.

    Повертає:
        float: Час, витрачений на виконання завдання.
    """
    counter = n
    start = time()  # Записуємо початковий час
    while counter > 0:  # Цикл, що зменшує лічильник до 0
        counter -= 1
    return time() - start  # Повертаємо час виконання

# Асинхронна функція для моніторингу


async def monitoring():
    """
    Постійно виводить повідомлення про стан моніторингу кожні 2 секунди.
    """
    while True:
        await asyncio.sleep(2)  # Чекаємо 2 секунди
        print(f'Monitoring {time()}')  # Виводимо час виконання

# Асинхронна функція для запуску блокуючих завдань у окремих потоках


async def run_blocking_tasks(executor, n):
    """
    Виконує блокуючу задачу у виділеному потоці.

    Аргументи:
        executor (concurrent.futures.ThreadPoolExecutor): Виконавець для запуску потоків.
        n (int): Початкове значення лічильника для блокуючого завдання.

    Повертає:
        float: Результат роботи блокуючого завдання (час виконання).
    """
    loop = asyncio.get_event_loop()  # Отримуємо поточний подієвий цикл
    print('waiting for executor tasks')
    # Виконуємо функцію blocks у потоці
    result = await loop.run_in_executor(executor, blocks, n)
    return result  # Повертаємо результат

# Основна асинхронна функція


async def main():
    """
    Запускає блокуючі завдання у потоках і моніторинг одночасно.
    """
    # Створюємо асинхронне завдання для функції моніторингу
    asyncio.create_task(monitoring())

    # Створюємо виконавця з трьома робочими потоками
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Запускаємо кілька блокуючих завдань із різними значеннями n
        futures = [run_blocking_tasks(executor, n)
                   for n in [50_000_000, 60_000_000, 70_000_000]]

        # Чекаємо завершення всіх завдань і збираємо результати
        results = await asyncio.gather(*futures)
        return results

# Основний блок виконання
if __name__ == '__main__':
    """
    Запускає основну асинхронну функцію main за допомогою asyncio.run.
    """
    result = asyncio.run(main())  # Запускаємо основну функцію
    for r in result:  # Виводимо результати кожного блокуючого завдання
        print(r)
