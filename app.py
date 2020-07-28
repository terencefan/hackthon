import json

from flask import Flask
app = Flask("ref")

@app.route('/image', methods=["POST"])
def recognize():
    from flask import request
    data = request.files['file']

    from api import image
    r = image(data)

    # return json.dumps(r)

    return json.dumps([
        {
            "name": u"Apple",
            "count": 1,
            "expireTime": 7 * 24 * 60
        },
        {
            "name": u"Orange",
            "count": 1,
            "expireTime": 7 * 24 * 60
        }
    ])


@app.route('/barcode', methods=["POST"])
def query():
    from flask import request
    code = request.json.get("codeNumber")
    if code is None:
        raise Exception("invalid barcode number")

    from api import barcode
    r = barcode(code)

    return json.dumps(r)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7020, debug=True)
