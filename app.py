import json

from flask import Flask
app = Flask("ref")

@app.route('/image', methods=["POST"])
def recognize():
    from flask import request

    from api import image
    r = image(request.get_data())

    return json.dumps(r)


@app.route('/barcode', methods=["POST"])
def query():
    from flask import request

    from api import barcode
    code = request.data.decode('utf-8')
    r = barcode(code)

    return json.dumps(r)


if __name__ == "__main__":
    app.run(port=7020, debug=True)
