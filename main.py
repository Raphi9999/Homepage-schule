from flask import Flask, render_template, redirect, request, session
from dotenv import load_dotenv; load_dotenv()
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "abcdefghijklmnopqrstuvwxyz"

ANSWER_KEY = [
    "answer_4",
    "answer_2",
    "answer_2",
    "answer_3",
    "answer_3",
]


# DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PUBLIC_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class QuizParticipant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    pts = db.Column(db.Integer)


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
    if not session.get("pts", None):
        return render_template("quiz.html")

    leaderboard = QuizParticipant.query.order_by(QuizParticipant.pts.desc()).limit(10).all() #letzte 10 nach pts geordnet

    return render_template("quiz_done.html", pts=session.get("pts"), username=session.get("username"), leaderboard=leaderboard)

@app.route("/quiz/log_participant", methods=["POST"])
def quiz_log_participant():
    pts = 0

    for i in range(5):
        if request.form.get(f"q{i+1}") == ANSWER_KEY[i]:
            pts += 1

    username = request.form.get("username").strip()

    session["pts"] = pts
    session["username"] = username

    obj = QuizParticipant(username=username, pts=pts)
    db.session.add(obj)
    db.session.commit()

    return redirect("/quiz")

@app.route("/sources")
def sources():
    return render_template("sources.html")


if __name__ == "__main__":
    app.run(debug=True)





# "Bauplan" definieren
class Schwein():
    def __init__(self):
        # Standarddaten für Schwein definieren
        self.hoehe = 1.05
        self.beine = 4
        self.lieblingsessen = ["Eier", "Karotten", "Altes Menschenessen"]
        self.nasenloecher = 2
        self.name = "Schweini"
        self.freunde = 0
        self.hunger = 10
    
    # Funktion um zu essen
    def essen(self, essen):
        # Checken, ob das Schwein das gegebene Essen mag.
        if essen in self.lieblingsessen:
            self.hunger -= 1
            return "<dankbares Grunzen>"
        else:
            return "<wütend> Grunz Grunz!"


# Schwein instanzieren
schweinchen_objekt = Schwein()


"""
Dieses "schweinchen_objekt" hat jetzt alle oben definierten Attribute. Es hat auch die Funktion "essen".
Es hat eine Höhe von 1.05, 4 Beine und die Lieblingsessen Eier, Karotten und Altes Menschenessen gespeichert.
Wenn man auf diese Daten zugreifen will, macht man das über das schweinchen_objekt. 
Wenn man das Schweinchen mit schweinchen_objekt.essen("Karotte") etwas essen lässt, würde der Hunger um einen Punkt
weniger werden, da Karotten zu seinem Lieblingsessen gehören.
"""
