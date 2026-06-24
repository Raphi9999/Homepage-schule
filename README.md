# Website über Programmiersprachen

### (Backend):
- Kein wirkliches Separates Backend wie es z.B. mit Django ginge, da dafür ein echtes Frontend-Framework notwendig wäre
- Micro-Framework Flask
- nur GET-Endpoints bis auf den POST-Endpoint für das Mitschreiben der Quiz-Teilnehmer
- PostgreSQL-Datenbank (über Flask-Sqlalchemy Library)

### Frontend:
- Navbar und Tabellen über Bootstrap
- Sonst ganz einfaches HTML und CSS
- HTML Templates über Flask-Jinja (erkennt man an "{}")
- If-Statements innerhalb des HTML ebenfalls über Flask-Jinja

### Testen
Testen kann man die Website, wenn man mit "pip install -r requirements.txt" alle 
nötigen Libraries installiert. Damit die Verbindung zur Datenbank hergestellt werden kann,
müsste man eine eigene .env-Datei anlegen mit der Public URL der Datenbank. Dann könnte
man mit "python main.py" die Website im Developer-Modus starten. Sie läuft dann standardmäßig
auf http://127.0.0.1:5000 (bzw. http:localhost:5000).

### Deployment
Die Website ist über den Cloud-Provider Railway gehostet. Sie ist zu finden unter: "https://homepage-schule-prod.up.railway.app"
Dort liegt logischerweise auch die Datenbank.



