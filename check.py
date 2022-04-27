import sqlite3

import requests

from app import DATABASE


def main():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    for domain in db.execute("SELECT * FROM domains").fetchall():
        is_up = False
        try:
            response = requests.head(domain["name"], allow_redirects=True)
        except requests.RequestException:
            pass
        else:
            is_up = response.status_code == 200

        db.execute(
            "UPDATE domains SET is_up=?, last_check=datetime('now') WHERE name=?",
            (int(is_up), domain["name"]),
        )
    db.commit()


if __name__ == "__main__":
    main()
