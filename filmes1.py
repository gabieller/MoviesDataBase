import pandas as pd
import requests
import json
import datetime as dt
import api

MOVIE_DETAILS = "https://api.themoviedb.org/3/movie/"

df = pd.read_csv("Filmes2.csv")


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


#genres = [{"id": 0, "name": "drama"}, {"id": 2, "name": "horror"}]

def format_genres(website_genre_list):
    teste = []
    separator = "|"
    for movie_item in website_genre_list:
        genre_dict = {'genres': movie_item['genres'], }
        only_genres = [d.get('name')
                       for sublists in genre_dict.values() for d in sublists]
        print (teste.append(only_genres))

    for sublists in teste:
        values = separator.join(str(v) for v in sublists)
        return(values)


def extract_data(website_movies_list):
    result_movies = []
    genres = format_genres(get)
    print(genres)
    for movie in website_movies_list:
        dict_movie = {
            "vote_average": (movie["vote_average"]/2),
            'vote_count': movie['vote_count'],
            'runtime': movie['runtime'],
            'genres': genres,
            'budget': movie['budget'],
            'revenue': movie['revenue']
        }
        result_movies.append(dict_movie)
    return result_movies


def change_csv(csv, values_dict):
    for movie in csv.iterrows():
        for values in values_dict:
            csv["Vote Average"] = [d['vote_average'] for d in data]
            csv["Vote Count"] = [d['vote_count'] for d in data]
            csv["Runtime"] = [d['runtime'] for d in data]
            csv["Genres"] = [d['genres'] for d in data]
            csv["Budget"] = [d['budget'] for d in data]
            csv["Revenue"] = [d['revenue'] for d in data]
    csv.to_csv("Movies_new.csv", index=True)
    return csv


get = movies(df)
formated = format_genres(get)

print(formated)

data = extract_data(get)
csv = change_csv(df,data)
print(csv.head())



# formated = format_genres(genres)
# print(formated)
# # formated tem que ser igual 'drama|horror'