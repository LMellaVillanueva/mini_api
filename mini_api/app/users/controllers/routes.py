from flask import jsonify, request, Blueprint
from app.users.model.User import User
from statistics import mean
import re

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data_user = request.get_json()
    new_user = User.insert_user(data_user)

    if new_user:
        return jsonify({ "created_user": new_user }), 201
    else: return jsonify({ "error": "Error en la conexión" }), 500

@user_bp.route('/all_users', methods=['GET'])
def all_users():
    all_users = User.get_all_users()

    if not all_users:
        return jsonify({ "error": 'Error en la conexión' }), 500

    return jsonify({ "all_users": all_users }), 200

@user_bp.route('/stats/<prop>', methods=['GET'])
def stats(prop):
    all_users = User.get_all_users()

    if not all_users:
        return jsonify({ "error": 'Error en la conexión' }), 500

    all_ages = [x['age'] for x in all_users]

    def filter_users(users_list, condition):
        return [x for x in users_list if condition(x)]

    match prop:
        case 'users':
            return jsonify({ "users": all_users }), 200

        case 'actives':
            users = filter_users(all_users, lambda user: user.get('active') is True and user.get('age', 0) >= 18)
            #! Lógica antigua
            # all_actives = [x for x in all_users if x['active'] and x['age'] >= 18]
            return jsonify({ "users": users }), 200

        case 'email':
            regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            # all_emails = [x for x in all_users if re.fullmatch(regex_email, x['email'])]
            users = filter_users(all_users, lambda user: re.fullmatch(regex_email, user.get('email', '')) is not None)
            return jsonify({ "users": users }), 200

        case 'mean':
            val_mean = mean(all_ages) if all_ages else 0
            user = [{
                "id": "AVG",
                "name": "PROMEDIO DE EDADES",
                "email": "N/A",
                "age": round(val_mean, 2),
                "active": True
            }]
            return jsonify({ "users": user }), 200
        
        case 'all_actives':
            # all_actives = [x for x in all_users if x['active']]
            users = filter_users(all_users, lambda user: user.get('active'))
            return jsonify({ "users": users }), 200

        case 'all_inactives':
            # all_inactives = [x for x in all_users if not x['active']]
            users = filter_users(all_users, lambda user: user.get('active') is False)
            return jsonify({ "users": users }), 200

        case 'max_age':
            # max_age_users = [x for x in all_users if x['age'] == max_age]
            max_age = max(all_ages)
            users = filter_users(all_users, lambda user: user.get('age') == max_age)
            return jsonify({ "users": users }), 200

        case 'min_age':
            # min_age_users = [x for x in all_users if x['age'] == min_age]
            min_age = min(all_ages)
            users = filter_users(all_users, lambda user: user.get('age') == min_age)
            return jsonify({ "users": users }), 200

        case _:
            return jsonify({ "error": f"Propiedad '{prop}' no válida" }), 400

@user_bp.route('/update', methods=['POST'])
def update_user():
    data = request.get_json()
    updated_user = User.update_user(data)
    if not updated_user:
        return jsonify({ "error": 'Error en la base de datos' }), 500
    return jsonify({ "updated_user": True }), 200

@user_bp.route('/delete', methods=['POST'])
def delete_user():
    data = request.get_json()
    deleted_user = User.delete_user(data['id'])
    if not deleted_user:
        return jsonify({ "error": 'Error en la base de datos' }), 500
    return jsonify({ "deleted_user": True }), 200