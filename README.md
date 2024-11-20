Flask ELO Matchmaking API

Flask projekat za upravljanje igračima, timovima i mečevima.

Opis okruženja potrebnog da se uradi build:

Za pokretanje i build aplikacije potrebno je sledeće:

Python 3.9 ili noviji: Preporučuje se korišćenje virtualnog okruženja (virtual environment) za instalaciju zavisnosti.
Pip: Alat za upravljanje Python paketima.
SQLite: Default baza podataka za lokalno okruženje.
Dodatni paketi:
        Flask
        Flask-SQLAlchemy
        Flask-Migrate
        Flask-CORS
        Python-Dotenv
        Pytest (za testiranje)

Svi potrebni paketi nalaze se u fajlu requirements.txt.

Kako se radi build:
Koraci:

Kloniranje repozitorijuma

    git clone https://github.com/jkovvv/elo-matchmaking-backend.git

Postavljanje virtualnog okruženja

    python -m venv venv
    source venv/bin/activate  # Na Windows-u: venv\Scripts\activate

Instalacija zavisnosti

    pip install -r requirements.txt

Kreiranje baze i migracija

    flask db init
    flask db upgrade

Primer kako se aplikacija pokreće:

Aktiviraj virtualno okruženje:

    source venv/bin/activate  # Na Windows-u: venv\Scripts\activate

Pokreni Flask development server:

    flask run

    Aplikacija će biti dostupna na http://127.0.0.1:5000/.

Lista korišćenih tehnologija sa kratkim opisom

Flask: Mikroframework za razvoj web aplikacija u Pythonu. Omogućava jednostavno pravljenje REST API servisa.
Flask-SQLAlchemy: Ekstenzija za Flask koja pruža ORM podršku za rad sa bazom podataka.
Flask-Migrate: Alat za upravljanje migracijama baze podataka pomoću Alembic biblioteke.
SQLite: Relaciona baza podataka koja je jednostavna za lokalni razvoj i ne zahteva dodatnu instalaciju.
