import pandas as pd
import requests
import json
import datetime as dt
import api

MOVIE_DETAILS = "https://api.themoviedb.org/3/movie/"

#df = pd.read_csv("Filmes.csv")
df = pd.read_csv("Filmes2.csv")

#Pegando o arquivo com os ID
#O que isso tá fazendo
def get_movie_info(id):
    params = {'api_key': api.API_KEY}
    res = requests.get(
        "https://api.themoviedb.org/3/movie/"+str(id), params=params)
    json = res.json()
    #title = json['title']
    # average = json['vote_average']
    # genres = json['genres'][0]['name']
    return json


def movies(csv):
    results = []
    for index, row in csv.iterrows():
        movie_title = row["FILME"]
        print(f"Buscando {movie_title}")
        movie_id = row["ID"]
        movie_info = get_movie_info(movie_id)
        results.append(movie_info)
    return results


def format_date(date):
    return dt.datetime.strptime(date, '%Y-%m-%d')


def get_user_average(list_id, csv):
    for movie, row in csv.iterrows():
        csv_id = row["ID"]
        movie_id = movie["id"]
        print(movie_id)
        # if movie_id == csv_id:
        #     user_average = row["NOTA"]
        #     return user_average


def extract_data(website_movies, csv_data):
    result_movies = []
    for movie in website_movies:
        movie_date = movie["release_date"]
        movie_year = format_date(movie_date).year
        average_user = get_user_average(website_movies, csv_data)
        tuple_movie = (
            movie["id"],
            movie_year,
            movie['vote_average'],
            average_user,
            movie['budget'],
        )
        result_movies.append(tuple_movie)
    return result_movies


get = movies(df)

#get_user_average(get, df)

# #info = movies(df)

# #get_user_average(info, df)
# #print(get_user_average)

# # get_user_average()

data = extract_data(get,df)
# print(data)
