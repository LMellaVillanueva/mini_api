from app.config.db_connection import get_connection
import psycopg2.extras

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.active = data['active']
        self.email = data['email']

    @classmethod
    def insert_user(cls, data):
        connect = get_connection()

        try:
            cursor = connect.cursor()

            new_user = cursor.execute('INSERT INTO users (name, age, active, email) VALUES (%(name)s, %(age)s, %(active)s, %(email)s) RETURNING id;', data)
            user_id = cursor.fetchone()[0]

            connect.commit()
            return user_id

        except Exception as error:
            connect.rollback()
            print('Error al insertar usuario: ', error)
            return None
        
        finally:
            cursor.close()
            connect.close()

    @classmethod
    def get_all_users(cls):
        conn = get_connection()
        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute('SELECT * FROM users;')
            rows = cursor.fetchall()
            return rows

        except Exception as error:
            conn.rollback()
            print('Error al obtener usuarios: ', error)
            return None

        finally:
            cursor.close()
            conn.close()

    @classmethod
    def update_user(cls, data):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET name = %(name)s, age = %(age)s, active = %(active)s, email = %(email)s WHERE id = %(id)s;', data)
            conn.commit()
            return False if cursor.rowcount == 0 else True

        except Exception as error:
            conn.rollback()
            print('Error al actualizar usuario: ', error)
            return None
            
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def delete_user(cls, id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = %(id)s;', { 'id': id })
            conn.commit()
            return False if cursor.rowcount == 0 else True

        except Exception as error:
            conn.rollback()
            print('Error al actualizar usuario: ', error)
            return None

        finally:
            cursor.close()
            conn.close()