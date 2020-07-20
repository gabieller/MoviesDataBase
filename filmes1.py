import pandas as pd
import requests
import json
import datetime as dt
import api

MOVIE_DETAILS = "https://api.themoviedb.org/3/movie/"

df = pd.read_csv("Movies.csv")


def format_date(date):
    return dt.datetime.strptime(date, '%Y-%m-%d')

# Pegando o arquivo com os ID
# O que isso tá fazendo


def get_movie_info(id):
    params = {'api_key': api.API_KEY}
    res = requests.get(
        "https://api.themoviedb.org/3/movie/"+str(id), params=params)
    json = res.json()
    #title = json['title']
    # average = json['vote_average']
    # genres = json['genres'][0]['name']
    return json

# Função tá pegando um csv e a partir dele buscando os filmes do csv no database a partir do ID do csv


def movies(csv):
    results = []
    for index, row in csv.iterrows():
        movie_title = row["Movie"]
        print(f"Buscando {movie_title}")
        movie_id = row["ID"]
        movie_info = get_movie_info(movie_id)
        results.append(movie_info)
    return results


def format_genres(genres):
    names = []
    for genre in genres:
        names.append(genre['name'])
    for i, genre in enumerate(names):
        if genre == "Science Fiction":
            names[i] = 'SciFi'
    return "|".join(names)


def extract_data(website_movies_list):
    result_movies = []
    for movie in website_movies_list:
        dict_movie = {
            "vote_average": (movie["vote_average"]/2),
            'vote_count': movie['vote_count'],
            'runtime': movie['runtime'],
            'genres': format_genres(movie['genres']),
            'budget': movie['budget'],
            'revenue': movie['revenue']
        }
        result_movies.append(dict_movie)
    return result_movies


def change_csv(csv, values_dict):
    for movie in csv.iterrows():
        for values in values_dict:
            csv["Vote Average"] = [d['vote_average']
                                   for d in getting_information]
            csv["Vote Count"] = [d['vote_count'] for d in getting_information]
            csv["Runtime"] = [d['runtime'] for d in getting_information]
            csv["Genres"] = [d['genres'] for d in getting_information]
            csv["Budget"] = [d['budget'] for d in getting_information]
            csv["Revenue"] = [d['revenue'] for d in getting_information]
    csv.to_csv("Movies_new.csv", index=False)
    return csv


seaching_movies = movies(df)
getting_information = extract_data(seaching_movies)
new_csv = change_csv(df, getting_information)
print(new_csv.head())


#formated = format_genres(seaching_movies)
