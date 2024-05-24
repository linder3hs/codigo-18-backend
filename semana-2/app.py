from flask import Flask, jsonify, request


app = Flask(__name__) # __name__ == '__main__'

users = []

@app.route('/')
def home():
    return jsonify(users)

"""
Vamos a hacer un ejemplo donde vamos a recibir la informacion del usuario pero
desde POSTMAN
"""
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    users.append(user_data)

    return jsonify({
        "new_user": user_data
    })



if __name__ == '__main__':
    app.run(port=7000, debug=True)
