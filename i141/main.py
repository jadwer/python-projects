import pandas as pd
from flask import Flask, jsonify, request

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)


all_movies = movies_data[['original_title', 'poster_link','release_date', 'runtime', 'weighted_rating']]

# print(all_movies.head(3))

liked_movies = []
not_liked_movies = []
did_not_watch = []

a_val = 123412321
b_val = 7653532
suma =  a_val + b_val

def assign_val() :
    m_data = {
        'original_title': all_movies.iloc[0,0],
        'poster_link': all_movies.iloc[0,1],
        'release_date': all_movies.iloc[0,2] or "N/A", 
        'duration': all_movies.iloc[0,3],
        'rating': all_movies.iloc[0,4]/2
    }
    return m_data

@app.route("/")
def home() :
    return jsonify({
        "data": "runing...",
        "status": "success"
    })

@app.route("/movies")
def get_movie() :
    movie_data = assign_val()

    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/like", methods=["POST", "GET"])
def liked_movie() :
    global all_movies
    movie_data = assign_val()
    liked_movies.append(movie_data)
    all_movies.drop([0], inplace=True)
    all_movies = all_movies.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

@app.route("/dislike", methods=["POST"])
def unliked_movie() :
    global all_movies

    movie_data = assign_val()
    not_liked_movies.append(movie_data)
    all_movies.drop([0], inplace=True)
    all_movies = all_movies.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

@app.route("/did_not_watch", methods=["POST"])
def did_not_watch_view() :
    global all_movies

    movie_data = assign_val()
    did_not_watch.append(movie_data)
    all_movies.drop([0], inplace=True)
    all_movies = all_movies.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })



if __name__ == "__main__" :
    app.run()