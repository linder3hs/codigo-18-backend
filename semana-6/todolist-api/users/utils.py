from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# esta funcion es para crear token


def get_tokens_for_user(user):
    tokens = RefreshToken.for_user(user)

    return {
        # refresh sera usando en un futuro para volver crear un nuevo token
        # cuando el original expire
        'refresh': str(tokens),
        # lo que usaremos hoy sera el access_token
        'access': str(tokens.access_token)
    }


# esta funcion para validar token
def validate_token(token):
    try:
        # UntypedToken: Va a decirnos si el token es valido o no
        # si al tratar de verificar que el token sea valido, este no lo es entonces
        # entrara en un error
        UntypedToken(token)
        return True
    except (InvalidToken, TokenError) as e:
        print(e)
        return False


def get_payload_from_token(token):
    try:
        return AccessToken(token).payload
    except (InvalidToken, TokenError) as e:
        print(e)
        return None
