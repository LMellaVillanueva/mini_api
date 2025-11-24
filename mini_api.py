import re
from statistics import mean

users = [
    {"name": "Ana", "age": 25, "active": True,  "email": "ana@example.com"},
    {"name": "Luis", "age": 17, "active": True,  "email": "luis_123@example.com"},
    {"name": "Marta", "age": 30, "active": False, "email": "marta@mail"},
    {"name": "Pedro", "age": 22, "active": True,  "email": "pedro@example.com"},
    {"name": "Sofia", "age": 16, "active": False, "email": "sofia@@example.com"},
    {"name": "Jorge", "age": 40, "active": True,  "email": "jorge@example.com"},
    {"name": "Elena", "age": 19, "active": True,  "email": "elena.mail.com"},
    {"name": "Raul", "age": 50, "active": False, "email": "raul@example.com"},
    {"name": "Julia", "age": 29, "active": True,  "email": "julia@example.com"},
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

estadistics(users)
