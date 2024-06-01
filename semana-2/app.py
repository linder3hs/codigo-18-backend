from flask import Flask, jsonify, request
from utils import encrypt_password
from config import Config
from extensions import db, migrate
from entities.user_model import User
from flask_cors import CORS


app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config)

CORS(app)

db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def home():
    return jsonify([])


# GET
@app.route('/api/v1/user')
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
@app.route('/api/v1/user/<int:user_id>')
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
@app.route('/api/v1/user', methods=['POST'])
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
@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
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


@app.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=7000, debug=True)
