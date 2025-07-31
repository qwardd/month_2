import sqlite3


def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("DROP TABLE IF EXISTS genres")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)


    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            FOREIGN KEY(genre_id) REFERENCES genres (id)
        )
    """)

def insert_genre(name):
    conn.execute(
        """
        INSERT INTO genres (name)
        VALUES (?)    
    """,
        (name,)
    )
    conn.commit()



def get_all_genres():
    results = conn.execute("""
    SELECT a.id, a.name, b.name FROM genres AS a
    INNER JOIN books AS b ON a.id = b.genre_id
            """)
    return results


def insert_book(name, author, publication_year,  number_of_pages, number_of_copies, genre_id):
    conn.execute(
        """
        INSERT INTO books (name, author, publication_year,  number_of_pages, number_of_copies, genre_id)
        VALUES (?, ?, ?, ?, ?,?)
        """,
        (name, author, publication_year, number_of_pages, number_of_copies, genre_id ))

    conn.commit()

def get_books():
    results = conn.execute("SELECT * FROM books")
    return results

if __name__ == '__main__':
    conn = sqlite3.connect('database.sqlite3')
    create_table()

    insert_book("Мертвые души", "Гоголь", 1842,  352, 32, 1)
    insert_book("Война и мир", "Толстой", 1867 ,  1696 , 267, 1)
    insert_book("Мастер и Маргарита", 'Булгаков', 1940,  480, 76, 2)
    insert_book('Отцы и дети', 'Тургенев', 1861, 288, 46,2)
    insert_book('Вишневый сад','Чехов', 1903,  224, 76, 2 )
    insert_book('Евгений Онегин', 'Пушкин', 1831, 272 , 87,3 )
    insert_book('Лето в городе', 'Пастернак', 1953,  320, 65, 3)
    insert_book('Преступление и наказание', 'Достоевский', 1867, 672, 47, 1 )
    insert_book('Старуха Изергиль', 'Горький ', 1894, 125, 16, 2 )
    insert_book('Идиот', 'Достоевский', 1869, 640, 57, 3 )


    insert_genre("роман")
    insert_genre("рассказ")
    insert_genre("повесть")

    for book in get_books():
        print(book)

    for genre in get_all_genres():
        print(genre)


    conn.close()
    
