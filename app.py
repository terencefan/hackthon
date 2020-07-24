import json

from flask import Flask
app = Flask("ref")

@app.route('/image', methods=["POST"])
def recognize():
    from flask import request
    print(request.get_data())

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
    print(request.get_data())

    return json.dumps({
        "name": u"Orange",
        "count": 1,
        "expireTime": 7 * 24 * 60,
    })


if __name__ == "__main__":
    app.run(port=7020, debug=True)
