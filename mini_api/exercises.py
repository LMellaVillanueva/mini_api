"""
    Ejercicios en los que me basé para crear las rutas del backend.
    Mismos endpoints, misma lógica.
"""

import re
from statistics import mean

users = [
    {"name": "Ana", "age": 25, "active": True,  "email": "ana@example.com"},
    {"name": "Luis", "age": 17, "active": True,  "email": ""},
    {"name": "Marta", "age": 0, "active": False, "email": "marta@mail"},
    {"name": "Pedro", "age": 22, "active": True,  "email": "pedro@example.com"},
    {"name": "Sofia", "age": 16, "active": False, "email": ""},
    {"name": "Jorge", "age": 0, "active": True,  "email": "jorge@example.com"},
    {"name": "Elena", "age": 19, "active": True,  "email": "elena.mail.com"},
    {"name": "Raul", "age": 50, "active": False, "email": "raul@example.com"},
    {"name": "Julia", "age": 0, "active": True,  "email": "julia@example.com"},
    {"name": "Tomas", "age": 15, "active": True,  "email": "tomas@@@mail.com"},
]

def users_actives(users):
    return print([x['name'].upper() for x in users if x['active'] == True and x['age'] >= 18])

def email_validate(users):
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b';
    return print([x['name'].upper() for x in users if re.fullmatch(regex_email, x['email'])])

def all_names(users):
    return print([x['name'].lower() for x in users])

def estadistics(users):
    all_estadistics = {}

    # Promedio
    all_ages = [x['age'] for x in users]
    all_estadistics['promedio'] = mean(all_ages)

    # Activos/Inactivos
    all_estadistics['actives'] = [x['name'].upper() for x in users if x['active']]
    all_estadistics['inactives'] = [x['name'].upper() for x in users if not x['active']]

    # Edad máxima/mínima
    max_age = max(all_ages)
    all_estadistics['max_age'] = [x['name'].upper() for x in users if x['age'] >= max_age]

    min_age = min(all_ages)
    all_estadistics['min_age'] = [x['name'].upper() for x in users if x['age'] <= min_age]

    return print(all_estadistics)

def email_errors(users):
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    i = 0
    fake_email_users = []
    while i < len(users):
        if not re.fullmatch(regex_email, users[i]['email']):
            fake_email_users.append({
            'user': users[i]['name'],
            'email': users[i]['email']
            })
        i += 1
    print(fake_email_users)

def lack_age_email(users):
    i = 0
    lack_age = []
    lack_email = []

    while i < len(users):
        if users[i]['age'] == 0:
            lack_age.append(users[i]['name'])

        if not users[i]['email']:
            lack_email.append(users[i]['name'])
        i += 1
    print('NOT AGED USERS', lack_age)
    print('NOT EMAIL USERS', lack_email)