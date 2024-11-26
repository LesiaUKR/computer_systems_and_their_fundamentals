import asyncio  # Імпортуємо asyncio для роботи з асинхронним програмуванням
from time import time  # Імпортуємо time для вимірювання часу виконання

# Список імітованих користувачів із їхніми даними
fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc',
        'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith',
        'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller',
        'email': 'alancoleman@example.net'}
]

# Асинхронна функція для отримання користувача за id


async def get_user_async(uid: int) -> dict:
    """
    Імітує асинхронний пошук користувача за id.

    Аргументи:
        uid (int): Ідентифікатор користувача.

    Повертає:
        dict: Дані знайденого користувача.
    """
    await asyncio.sleep(0.5)  # Імітуємо затримку (наприклад, запит до сервера)
    # Фільтруємо користувачів за id
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user  # Повертаємо знайденого користувача

# Основна асинхронна функція


async def main():
    """
    Викликає асинхронно функцію get_user_async для кожного користувача
    та виконує всі виклики паралельно.

    Повертає:
        list[dict]: Список даних користувачів.
    """
    r = []  # Список для збереження об'єктів coroutine
    for i in range(1, 4):  # Ітерація по id користувачів від 1 до 3
        r.append(get_user_async(i))  # Додаємо coroutine до списку
    # Виконуємо всі coroutine паралельно і збираємо результати
    return await asyncio.gather(*r)

# Основний блок виконання
if __name__ == '__main__':
    start = time()  # Записуємо початковий час виконання
    result = asyncio.run(main())  # Запускаємо основну асинхронну функцію
    for r in result:  # Ітеруємося по результатах
        print(r)  # Виводимо кожного користувача
    print(time() - start)  # Виводимо загальний час виконання
