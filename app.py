from flask import Flask, jsonify

from service.roll import roll_menu

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route("/")
def roll():
    result = roll_menu()
    return jsonify(result)


if __name__ == '__main__':

    app.run("0.0.0.0", 6080)

