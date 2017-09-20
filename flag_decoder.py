from flask import Flask, request
from jose import jwt
from jose.jwt import JWTError

from checker_key import CHECKER_KEY


BAD_REQUEST = 400

CAPSULE_PREFIX = 'VolgaCTF{'
CAPSULE_SUFFIX = '}'
ALGORITHM = 'ES256'

app = Flask(__name__)


class CapsuleDecodingError(ValueError):
    pass


def decode_capsule(capsule):
    if not capsule:
        raise CapsuleDecodingError('No data provided')
    if not (capsule.startswith(CAPSULE_PREFIX) and capsule.endswith(CAPSULE_SUFFIX)):
        raise CapsuleDecodingError('Capsule does not follow the format {prefix}...{suffix}'.format(
            prefix=CAPSULE_PREFIX,
            suffix=CAPSULE_SUFFIX))

    capsule_payload = capsule[len(CAPSULE_PREFIX): -len(CAPSULE_SUFFIX)]
    try:
        decoded = jwt.decode(capsule_payload, CHECKER_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        message = 'Error while decoding the token: {error}'.format(error=e)
        raise CapsuleDecodingError(message)

    flag = decoded.get('flag')
    if flag is None:
        raise CapsuleDecodingError('Capsule contains no flag')

    return flag


@app.route('/flag', methods=['GET', 'POST'])
def decode_capsule_endpoint():
    if request.method == 'GET':
        capsule = request.args.get('capsule')
    elif request.method == 'POST':
        try:
            capsule = request.get_data().decode('utf-8').strip()
        except Exception:
            return 'Could not decode POST data', BAD_REQUEST
    else:
        raise ValueError('Unsupported method: {}'.format(request.method))

    try:
        return decode_capsule(capsule)
    except CapsuleDecodingError as e:
        return str(e), BAD_REQUEST
