from flask import jsonify, request, Blueprint
from mini_api.users.model.User import User
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
    match prop:
        case 'users':
            return jsonify({ "all_users": all_users }), 200

        case 'actives':
            all_actives = [x['name'].upper() for x in all_users if x['active'] and x['age'] >= 18]
            return jsonify({ "actives_users": all_actives }), 200

        case 'email':
            regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            all_emails = [x['name'].upper() for x in all_users if re.fullmatch(regex_email, x['email'])]
            return jsonify({ "email_users": all_emails }), 200

        case 'mean':
            return jsonify({ "mean": mean(all_ages) }), 200
        
        case 'all_actives':
            all_actives = [x['name'].upper() for x in all_users if x['active']]
            return jsonify({ "all_actives": all_actives }), 200

        case 'all_inactives':
            all_inactives = [x['name'].upper() for x in all_users if not x['active']]
            return jsonify({ "all_inactives": all_inactives }), 200

        case 'max_age':
            max_age = max(all_ages)
            max_age_users = [x['name'].upper() for x in all_users if x['age'] == max_age]
            return jsonify({ "max_age": max_age_users }), 200

        case 'min_age':
            min_age = min(all_ages)
            min_age_users = [x['name'].upper() for x in all_users if x['age'] == min_age]
            return jsonify({ "min_age": min_age_users }), 200

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
    if not delete_user:
        return jsonify({ "error": 'Error en la base de datos' }), 500
    return jsonify({ "deleted_user": True }), 200