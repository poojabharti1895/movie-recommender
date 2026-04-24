import sqlite3
import hashlib

def connect():
    return sqlite3.connect("database/users.db", check_same_thread=False)

def create_user(username, password):
    conn = connect()
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()

def login_user(username, password):
    conn = connect()
    c = conn.cursor()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed))
    return c.fetchone()