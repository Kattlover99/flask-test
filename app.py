from flask import Flask, render_template, redirect, url_for
from flask_appbuilder import AppBuilder, SQLA
import sqlite3
import secrets
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = secrets.token_hex(16)
db = SQLA(app)

def get_db_connection():
    conn = sqlite3.connect('database.sqlite', check_same_thread=False)
    return conn

conn = get_db_connection()
appbuilder = AppBuilder(app, db.session)


@app.route('/get_movies_dump')
def get_movies_dump():
    try:
        subprocess.run(['python', 'get_data_from_wiki.py'])
        return 'Data loaded successfully'
    except Exception as error:
        return str(error)

@app.route('/create_movie_table')
def create_movie_table():
    try:
        conn.execute('CREATE TABLE movies (item_id TEXT PRIMARY KEY,item_label TEXT,imdb_id TEXT,date_of_release TEXT)')
        return 'Movie table created successfully'
    except: 
        return 'Movie table already exists'
    

@app.route('/movies')
def get_movies():
    # execute a SQL query to fetch all records from the movies table
    try: 
        c=conn.cursor()
        c.execute('SELECT * FROM movies')
        rows = c.fetchall()
        
        # convert the results to a list of dictionaries
        movies = []
        for row in rows:
            movie = {
                # 'id': row[0],
                'item_id': row[0],
                'item_label': row[1],
                'imdb_id': row[2],
                'date_of_release': row[3]
            }
            movies.append(movie)
        
        return render_template('movies.html', movies=movies)
    except Exception as error:
        return str(error)

if __name__ == '__main__':
    app.run(debug=True)

