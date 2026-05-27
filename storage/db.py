import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "users.db")

print(DB_PATH)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        style TEXT DEFAULT 'classic',
        effort INTEGER DEFAULT 5
    )
    """)

    conn.commit()
    conn.close()


def get_user(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT style, effort FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()

    conn.close()

    if row:
        return {"style": row[0], "effort": row[1]}

    return {"style": "classic", "effort": 5}


def upsert_user(user_id: int, style=None, effort=None):
    user = get_user(user_id)

    style = style or user["style"]
    effort = effort or user["effort"]

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (user_id, style, effort)
    VALUES (?, ?, ?)
    ON CONFLICT(user_id)
    DO UPDATE SET style=excluded.style, effort=excluded.effort
    """, (user_id, style, effort))

    conn.commit()
    conn.close()