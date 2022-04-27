import sqlite3

from app import DATABASE


def main():
    db = sqlite3.connect(DATABASE)
    db.execute(
        """CREATE TABLE IF NOT EXISTS domains (
        name TEXT,
        is_up BOOLEAN,
        last_check DATE
    )"""
    )


if __name__ == "__main__":
    main()
