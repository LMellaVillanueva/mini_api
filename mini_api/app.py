# from os import system
# if system("clear") != 0: system("cls")

from app import create_app
from app.config.db_connection import get_connection
from app.config.init_db import create_tables
from flask_cors import CORS

app = create_app()
create_tables()

CORS(app, resources={r"/*": {"origins": 'http://localhost:5173'}}, supports_credentials=True)

from app.users.controllers.routes import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

# Probar conexión a pg
try:
    connection = get_connection()
    if connection:
        print('CONECTADO A PG')
        connection.close()
    else: print('NO SE PUDO CONECTAR A PG')
except Exception as error:
    print('ERROR AL CONECTAR A PG:', error)

app.run(debug=True)