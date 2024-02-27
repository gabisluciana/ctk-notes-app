import sqlite3


def create_database_connection():
    try:
        conn = sqlite3.connect("notes.db")
        return conn
    except sqlite3.Error as err:
        print(f"Error connecting to the database: {err}")
        return None


def create_tables():
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                body TEXT NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating notes table: {err}")


def execute_query(query, params=()):
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
        return results
    except sqlite3.Error as err:
        print(f"Error executing query: {err}")
        return []
