from flask import Flask, jsonify, request
from utils import encrypt_password


app = Flask(__name__)  # __name__ == '__main__'


@app.route('/')
def home():
    return jsonify([])


@app.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_data['password'] = encrypt_password(
            user_data.get('password')).decode('utf-8')
        # users.append(user_data)

        return jsonify({
            "new_user": user_data
        })
    except Exception as e:
        return jsonify({
            "error": e,
            "linea": e.__traceback__.tb_lineno
        })


if __name__ == '__main__':
    app.run(port=7000, debug=True)
