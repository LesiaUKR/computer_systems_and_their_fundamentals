# Імпортуємо sleep для затримки і time для вимірювання часу виконання
from time import sleep, time

# Список імітованих користувачів із їхніми даними
fake_users = [
    {
        "id": 1,
        "name": "April Murphy",
        "company": "Bailey Inc",
        "email": "shawnlittle@example.org",
    },
    {
        "id": 2,
        "name": "Emily Alexander",
        "company": "Martinez-Smith",
        "email": "turnerandrew@example.org",
    },
    {
        "id": 3,
        "name": "Patrick Jones",
        "company": "Young, Pruitt and Miller",
        "email": "alancoleman@example.net",
    },
]

# Синхронна функція для отримання даних користувача за ідентифікатором


def get_user_sync(uid: int) -> dict:
    """
    Шукає користувача за унікальним ідентифікатором (uid) у списку fake_users.

    Аргументи:
        uid (int): Ідентифікатор користувача.

    Повертає:
        dict: Дані користувача.
    """
    sleep(0.5)  # Затримка для імітації тривалого процесу (наприклад, запиту до бази даних)
    # Використовуємо фільтр для пошуку користувача за його id
    (user,) = list(filter(lambda user: user["id"] == uid, fake_users))
    return user  # Повертаємо знайденого користувача


# Основний блок виконання
if __name__ == "__main__":
    start = time()  # Вимірюємо початковий час виконання
    for i in range(1, 4):  # Перебираємо id користувачів від 1 до 3
        # Викликаємо функцію для кожного користувача і виводимо його дані
        print(get_user_sync(i))
    # Виводимо загальний час виконання всіх викликів функції
    print(time() - start)
