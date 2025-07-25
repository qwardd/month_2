import sqlite3


def create_table():
    conn.execute("DROP TABLE IF EXISTS users")  # удаляем таблицу
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT
        )
    """)


def add_user(name, age, city):
    conn.execute(
        """
        INSERT INTO users(name, age, city)
        VALUES (?, ?, ?)
        """,
        (name, age, city),
    )
    conn.commit()


def get_all_users():
    result = conn.execute("SELECT * FROM users")
    return result


if __name__ == "__main__":
    # открываем соединение с базой данных
    conn = sqlite3.connect("../database.sqlite")
    # создаем таблицу
    create_table()

    # добавляем данные
    add_user("Aibek", 20, "Karakol")
    add_user("Sultan", 22, "Osh")

    # получаем данные
    for user in get_all_users():
        print(user)

    # закрываем соединение
    conn.close()