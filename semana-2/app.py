from flask import Flask, jsonify, request
from utils import encrypt_password
from config import Config
from extensions import db, migrate
from entities.user_model import User


app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config)

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
