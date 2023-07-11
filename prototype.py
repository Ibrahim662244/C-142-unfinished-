from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv("final.csv")
app = Flask(__name__)

liked_movies = []
not_liked_movies = []
did_not_watch = []

def assign_value():
    m_data = {
        "original_title": movies_data.iloc[0, 0],
        "poster_link": movies_data.iloc[0, 1],
        "release_date": movies_data.iloc[0, 2],
        "duration": movies_data.iloc[0, 3],
        "rating": movies_data.iloc[0, 4],
    }
    return m_data

@app.route("/movies")
def get_movie():
    if movies_data.empty:
        return jsonify({
            "message": "No more movies to display.",
            "status": "error"
        })

    movie_data = assign_value()
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/like")
def like_movie():
    if movies_data.empty:
        return jsonify({
            "message": "No more movies to like.",
            "status": "error"
        })

    liked_movie = assign_value()
    liked_movies.append(liked_movie)
    movies_data.drop(movies_data.index[0], inplace=True)
    return jsonify({
        "message": "Movie liked successfully.",
        "status": "success"
    })

@app.route("/dislike")
def dislike_movie():
    if movies_data.empty:
        return jsonify({
            "message": "No more movies to dislike.",
            "status": "error"
        })

    disliked_movie = assign_value()
    not_liked_movies.append(disliked_movie)
    movies_data.drop(movies_data.index[0], inplace=True)
    return jsonify({
        "message": "Movie disliked successfully.",
        "status": "success"
    })

@app.route("/skip")
def skip_movie():
    if movies_data.empty:
        return jsonify({
            "message": "No more movies to skip.",
            "status": "error"
        })

    skipped_movie = assign_value()
    did_not_watch.append(skipped_movie)
    movies_data.drop(movies_data.index[0], inplace=True)
    return jsonify({
        "message": "Movie skipped successfully.",
        "status": "success"
    })

@app.route("/liked-movies")
def get_liked_movies():
    return jsonify({
        "data": liked_movies,
        "status": "success"
    })

@app.route("/not-liked-movies")
def get_not_liked_movies():
    return jsonify({
        "data": not_liked_movies,
        "status": "success"
    })

@app.route("/did-not-watch")
def get_did_not_watch_movies():
    return jsonify({
        "data": did_not_watch,
        "status": "success"
    })

@app.route("/reset")
def reset_movies():
    global movies_data, liked_movies, not_liked_movies, did_not_watch
    movies_data = pd.read_csv("final.csv")
    liked_movies = []
    not_liked_movies = []
    did_not_watch = []
    return jsonify({
        "message": "Movies data reset successfully.",
        "status": "success"
    })

if __name__ == "__main__":
    app.run()