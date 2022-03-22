from flask import Flask
import random

app = Flask(__name__)

f = open("static/AssassinationList.txt", "r", encoding="utf8")

s = f.read()
assassination_list = s.split("\n")

f.close()

@app.route("/")
def roll():

    max = len(assassination_list)

    index = random.randint(0, max - 1)

    return assassination_list[index]


if __name__ == '__main__':

    app.run("0.0.0.0", 6080)

