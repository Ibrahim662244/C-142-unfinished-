from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv("final.csv")
app = Flask(__name__)

liked_movies = []
not_liked_movies = []
did_not_watch = []

def assign_value():
    m_data = {
        "original_title":all_movies.iloc[0,0],
        "poster_link":all_movies.iloc[0,1],
        "release_date":all_movies.iloc[0,2],
        "duration":all_movies.iloc[0,3],
        "rating":all_movies.iloc[0,4],
    }
    return m_data


@app.route("/movies")
def get_movie():
    movie_data=  assign_value()
    return jsonify({
        "data":movie_data,
        "status":success
    })




if __name__ == "__main__":
    app.run()