import sqlite3
from flask import g, Flask

app = Flask(__name__)

DATABASE = "db.sqlite3"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def get_domains():
    return query_db("""SELECT * FROM domains""")


@app.route("/")
def index():
    return {"/domains/": "Domain names to monitor."}


@app.route("/domains/")
def domains():
    return {
        "domains": [
            {
                "name": domain['name'],
                "is_up": bool(domain['is_up']),
                "last_check": domain['last_check'],
            }
            for domain in get_domains()
        ]
    }
