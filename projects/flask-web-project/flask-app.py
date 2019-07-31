from flask import Flask
from datetime import datetime
import csv
import json


"""
To run 

$ python flask-app.py

"""

filename = "/data/movielens/movies.csv"
with open(filename) as f:
    movies = list(csv.DictReader(f)) 
    #movies = [json.dumps(d) for d in movies]
    
print(movies)
print(type(movies))
print(type(movies[0]))

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"


@app.route('/now')
def current_time():
    return str(datetime.now())

@app.route('/movies')
def get_movies():
    return dict(records = movies)
    
@app.route('/movies/<movie_id>')
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["movieId"] == movie_id:
            return movie
    return dict(status = "ERROR", message = f"No movie has been found with {movie_id}"), 404


if __name__ == '__main__':
    app.run(debug=True)
    