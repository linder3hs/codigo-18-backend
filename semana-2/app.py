from flask import Flask, jsonify, request
import bcrypt


app = Flask(__name__) # __name__ == '__main__'

users = []


def encrypt_password(password):
    """
     Generar un salt
     salt: es un numero aleatorio que se genera y es concatenado al password,
     este se usa por seguridad y para evitar ataques de fuerza bruta
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)



@app.route('/')
def home():
    return jsonify(users)

"""
Vamos a hacer un ejemplo donde vamos a recibir la informacion del usuario pero
desde POSTMAN
"""
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
      user_data = request.get_json()
      user_data['password'] = encrypt_password(user_data.get('password')).decode('utf-8')
      users.append(user_data)

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
