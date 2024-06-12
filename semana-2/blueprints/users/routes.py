from flask import Blueprint, jsonify, request
from extensions import db
from entities.user_model import User
from utils import encrypt_password, check_password
from flask_jwt_extended import create_access_token, jwt_required

users_bp = Blueprint('users', __name__)

"""
Ruta para autentica a los usuarios:

email
password
"""


@users_bp.route('/api/v1/login', methods=['POST'])
def login():
    user_data = request.get_json()
    # paso1: Buscar al usuario por correo (email)
    user = User.query.filter_by(email=user_data["email"]).first()
    # paso2: Validar que el usuario exista
    if user is None:
        return jsonify({
            "message": "Email y/o password incorrectos"
        })

    print('password', user.password)
    # paso3: Usar una funcion que nos permita comparar el texto normal con el texto encriptado
    if check_password(user_data["password"].encode('utf-8'), user.password.encode('utf-8')):
        # paso 4 Si el usuario es correcto entonces creamos un token
        access_token = create_access_token(identity=user.id)
        return {
            "user": user.to_dic(),
            "access_token": access_token
        }
    else:
        return jsonify({
            "message": "Email y/o password incorrectos"
        })


@users_bp.route('/api/v1/user')
@jwt_required()
def get_all_users():
    try:
        users = User.query.all()
        dic_users = []

        for user in users:
            dic_users.append(user.to_dic())

        return jsonify({
            'users': dic_users
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500


# GET by user id
@users_bp.route('/api/v1/user/<int:user_id>')
@jwt_required()
def get_user_by_id(user_id):
    try:
        # buscamos al usuario por id
        user = User.query.get(user_id)

        if user is None:
            return jsonify({
                "message": "user not found"
            })

        return jsonify({
            "user": user.to_dic()
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500


# POST
@users_bp.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_data['password'] = encrypt_password(
            user_data.get('password')).decode('utf-8')

        new_user = User(
            full_name=f"{user_data['name']} {user_data['lastname']}",
            email=user_data['email'],
            password=user_data['password'],
            phoneNumber=user_data['phone_number'],
            genre=user_data['genre']
        )

        db.session.add(new_user)
        db.session.commit()  # COMMIT (SAVEPOINT)

        return jsonify({
            "new_user": new_user.to_dic()
        }), 201
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500


# UPDATE (PUT)
@users_bp.route('/api/v1/user/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    try:
        user_data = request.get_json()
        # buscar al usuario de nuestra base de datos y ver si existe
        user = User.query.get(user_id)

        if user is None:
            return jsonify({
                "message": "user not found"
            })

        # si, si existe entonces hacemos la actualizacion de los datos
        if 'full_name' in user_data:
            user.full_name = user_data['full_name']

        if 'email' in user_data:
            user.email = user_data['email']

        if 'password' in user_data:
            user.password = encrypt_password(
                user_data['password']).decode('utf-8')

        if 'phone_number' in user_data:
            user.phoneNumber = user_data['phone_number']

        if 'genre' in user_data:
            user.genre = user_data['genre']

        db.session.commit()
        return jsonify({
            "message": "user updated"
        })

    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500

# DELETE


@users_bp.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    try:
        # buscar por id
        user = User.query.get(user_id)

        if user is None:
            return jsonify({
                "message": "user not found"
            })

        # eliminar al usuario
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            "message": "user deleted"
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        }), 500
