import sqlite3

conn = sqlite3.connect('databse.sqlite3')

def create_table():
    conn.execute('DROP TABLE IF EXISTS genres')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT
    )
    """)
    conn.commit()

def insert_genre(genre):
    conn.execute(
        """
        INSERT INTO genres (genre)
        VALUES (?)
        """,
        (genre,)
    )
    conn.commit()

def get_genre():
    result = conn.execute('SELECT * FROM genres')
    return result

if __name__ == '__main__':
    conn = sqlite3.connect('databse.sqlite3')
    create_table()

    insert_genre('роман')
    insert_genre('рассказ')
    insert_genre('лирическое стихотворение ')

    for genre in get_genre():
        print(genre)

    conn.close()






