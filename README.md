# **Mini API**

Mini proyecto desarrollado para practicar la conexión de base de datos PostgreSQL y backend Python, empleando buenas prácticas y mejorando la lógica de programación.

---

## **Objetivo**

- El objetivo de este proyecto es mejorar mis prácticas de programación, entendiendo la conexión de Python con PostgreSQL. 
- Implementar un backend con Flask.
- Implementar métodos aprendidos, ya sea List Comprehension, Regex, bucles, entre otros.

---

## **Tecnologías usadas**
- Python 3.12
- Flask
- PostgreSQL
- psycopg2
- Python-dotenv

## **Ejemplo de uso**

Ejemplo de creación de un usuario mediante petición POST:

```http
    POST /users/register
```
```json

    {
      "name": "Juan",
      "age": 25,
      "active": true,
      "email": "juan@email.com"
    }
```

Respuesta esperada:

```json
    {
        "user_id": 1
    }
```

## **Ejecución del proyecto**

1. Clonar el repositorio
2. Crear y activar un entorno virtual:

```bash
    python -m venv nombre_de_tu_entorno
```

3. Instalar dependencias:

```bash
    pip install -r requirements.txt
```

4. Crear un archivo .env con las variables de entorno

```env
    PG_HOST=localhost
    PG_USER=tu_usuario
    PG_PASSWORD=tu_password
    PG_DATABASE=mini_api
    PG_PORT=5432
```

5. Crear las tablas ejecutando el script correspondiente.
6. Levantar el servidor:

```bash
    python app.py
```

---

## **Endpoints disponibles**

- POST /users/register → Crear usuario

- GET /users/all → Obtener todos los usuarios

- POST /users/update → Actualizar usuario

- POST /users/delete → Eliminar usuario

- GET /users/stats/<prop> → Estadísticas (edad, activos, emails válidos, etc.)

---

## **Progreso reciente**

- Refactorización de la lógica de filtrado de usuarios mediante la función reutilizable `filter_users`, evitando duplicación de código en múltiples endpoints.
- Implementación de funciones lambda para definir condiciones dinámicas de filtrado.
- Mejora en la validación de datos utilizando:
  - `.get()` para evitar errores por claves inexistentes.
  - Valores por defecto en campos opcionales.
  - Optimización de cálculos estadísticos:
  - Cálculo previo de valores como edad máxima y mínima para evitar recomputaciones innecesarias.
- Implementación de validación de emails mediante expresiones regulares (`re.fullmatch`).
- Código más legible y mantenible, alineado con buenas prácticas de backend.