import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            database = os.getenv('PG_DATABASE'),
            user = os.getenv("PG_USER"),
            host = os.getenv("PG_HOST"),
            password = os.getenv("PG_PASSWORD"),
            port = os.getenv("PG_PORT")
        )
        return conn
    except psycopg2.Error as error:
        print('ERROR AL CONECTAR A PG: ', error)
        return None