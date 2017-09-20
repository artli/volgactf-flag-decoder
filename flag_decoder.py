from flask import Flask, request, abort
from jose import jwt

from checker_key import CHECKER_KEY


PORT = 8090
CAPSULE_PREFIX = 'VolgaCTF{'
CAPSULE_SUFFIX = '}'
ALGORITHM = 'ES256'

app = Flask(__name__)


def decode_capsule(capsule):
    if not (capsule.startswith(CAPSULE_PREFIX) and capsule.endswith(CAPSULE_SUFFIX)):
        abort(500)
    capsule_payload = capsule[len(CAPSULE_PREFIX): -len(CAPSULE_SUFFIX)]
    decoded = jwt.decode(capsule_payload, CHECKER_KEY, algorithms=[ALGORITHM])
    return decoded['flag']


@app.route('/flag', methods=['GET', 'POST'])
def decode_capsule_endpoint():
    if request.method == 'GET':
        capsule = request.args.get('capsule')
    elif request.method == 'POST':
        capsule = request.get_data().decode('utf-8')
    else:
        abort(500)

    if not capsule:
        abort(400)
    return decode_capsule(capsule)


if __name__ == '__main__':
    app.run(port=PORT)
