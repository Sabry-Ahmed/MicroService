from typing import List, Dict
from flask import Flask,render_template, redirect, url_for, request
import json
import os 
import psycopg2




app = Flask(__name__)

def connect_to_db():
    try:
        url = os.getenv("DATABASE_URL")
        conn = psycopg2.connect(url)
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def test_table() -> List[Dict]:
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{login: mdp} for (login, mdp) in cursor]
    cursor.close()
    conn.close()

    return results

@app.route('/')
def index():
   return render_template('index.html',text=test_table())

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    go=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            go = 'Felicitation '+request.form['username'] 
    return render_template('index.html', error=error,go=go)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
