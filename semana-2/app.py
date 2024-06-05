from flask import Flask, jsonify
from config import Config
from extensions import db, migrate
from flask_cors import CORS
from blueprints.users.routes import users_bp


app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config)

CORS(app)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(users_bp)


@app.route('/')
def home():
    return jsonify([])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=7000, debug=True)
