import sqlite3


def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)



def insert_book(name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
        """
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (name, author, publication_year, genre, number_of_pages, number_of_copies),
    )
    conn.commit()

def get_books():
    results = conn.execute("SELECT * FROM books")
    return results

if __name__ == '__main__':
    conn = sqlite3.connect('database.sqlite3')
    create_table()

    insert_book("Мертвые души", "Гоголь", 1842, "поэма", 352, 32)
    insert_book("Война и мир", "Толстой", 1867 , 'роман', 1696 , 267)
    insert_book("Мастер и Маргарита", 'Булгаков', 1940, 'роман', 480, 76)
    insert_book('Отцы и дети', 'Тургенев', 1861,'роман', 288, 46)
    insert_book('Вишневый сад','Чехов', 1903, 'пьеса', 224, 76 )
    insert_book('Евгений Онегин', 'Пушкин', 1831,'роман', 272 , 87 )
    insert_book('Лето в городе', 'Пастернак', 1953, 'лирического стихотворения', 320, 65)
    insert_book('Преступление и наказание', 'Достоевский', 1867,'роман', 672, 47 )
    insert_book('Старуха Изергиль', 'Горький ', 1894,'Рассказ', 125, 16 )
    insert_book('Идиот', 'Достоевский', 1869,'роман', 640, 57 )
    

    for book in get_books():
        print(book)

    conn.close()
    
