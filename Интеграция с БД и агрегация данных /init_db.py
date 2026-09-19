import sqlite3


def initialize_database() -> None:
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS partners (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partner_type TEXT NOT NULL,
            name TEXT NOT NULL,
            director TEXT NOT NULL,
            phone TEXT NOT NULL,
            rating INTEGER NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sales_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            partner_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (partner_id) REFERENCES partners(id)
        )
        """
    )

    cursor.execute("DELETE FROM sales_history")
    cursor.execute("DELETE FROM partners")

    partners = [
        ("ООО", "Партнер А", "Иванов И.И.", "+7 900 111 11 11", 10),
        ("АО", "Партнер Б", "Петров П.П.", "+7 900 222 22 22", 8),
        ("ИП", "Партнер В", "Сидоров С.С.", "+7 900 333 33 33", 7),
        ("ООО", "Партнер Г", "Кузнецов К.К.", "+7 900 444 44 44", 9),
    ]

    cursor.executemany(
        """
        INSERT INTO partners (partner_type, name, director, phone, rating)
        VALUES (?, ?, ?, ?, ?)
        """,
        partners,
    )

    sales = [
        (1, 9999),
        (1, 1),
        (2, 49999),
        (2, 1),
        (3, 300000),
    ]

    cursor.executemany(
        """
        INSERT INTO sales_history (partner_id, quantity)
        VALUES (?, ?)
        """,
        sales,
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")
