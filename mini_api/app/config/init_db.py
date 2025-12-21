from app.config.db_connection import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            active BOOLEAN NOT NULL,
            email VARCHAR(100) NOT NULL
        );
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Tablas creadas correctamente")

if __name__ == "__main__":
    create_tables()
