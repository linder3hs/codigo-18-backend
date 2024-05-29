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
        db.session.commit()

        return jsonify({
            "new_user": new_user.to_dic()
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        })


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=7000, debug=True)
