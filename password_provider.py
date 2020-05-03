from flask import Flask
from flask import render_template
from flask import jsonify

from xkcdpass import xkcd_password as xp

app = Flask(__name__)

def generate_password(length=4, delimiter="-"):
    """returns a xkcd-style password"""
    wordfile = xp.locate_wordfile("ger-anlx")
    mywords = xp.generate_wordlist(
            wordfile=wordfile,
            min_length=3,
            max_length=16,
            valid_chars="[a-z]"
            )
    password = xp.generate_xkcdpassword(
            mywords,
            numwords=length,
            delimiter=delimiter,
            case="capitalize"
            )
    return password



@app.route("/rest/password")
def rest_password(length=4, delimiter="-"):
    return jsonify(generate_password(length=length, delimiter=delimiter))\

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    # debug does autoreloading of everything
    app.run(debug=True)



