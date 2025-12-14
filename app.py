# from os import system
# if system("clear") != 0: system("cls")

from mini_api import create_app
from mini_api.config.db_connection import get_connection
from mini_api.config.init_db import create_tables

app = create_app()
create_tables()

from mini_api.users.controllers.routes import user_bp
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