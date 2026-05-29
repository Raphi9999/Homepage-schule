from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/oop")
def oop():
    return render_template("oop.html")


@app.route("/script")
def scriptlangs():
    return render_template("scriptsprachen.html")


@app.route("/syntax")
def syntax():
    return render_template("syntax_semantik.html")


@app.route("/history")
def history():
    return render_template("geschichte.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(debug=True)