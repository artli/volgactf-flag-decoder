from flask import Flask, request, abort
import jwt

from checker_key import CHECKER_KEY


app = Flask(__name__)


def decode_capsule(capsule):
    return capsule + 'd'


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
    app.run(port=8090)
