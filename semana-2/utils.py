import bcrypt


def encrypt_password(password):
    """
     Generar un salt
     salt: es un numero aleatorio que se genera y es concatenado al password,
     este se usa por seguridad y para evitar ataques de fuerza bruta
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)
