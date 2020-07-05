import pandas as pd

base = pd.read_csv("Filmes2.csv")

data = [
    {"budget": 139353, "director": "Jonas"}, {"budget": 2, "director": "Pedro"},
    {"budget": 3, "director": "Jonas"}, {"budget": 4, "director": "Gilberto"},
    {"budget": 5, "director": "João"}, {"budget": 6, "director": "Pedro"},
    {"budget": 7, "director": "Jonas"}, {"budget": 8, "director": "Gilberto"},
    {"budget": 9, "director": "João"}, {"budget": 10, "director": "Pedro"},
    {"budget": 11, "director": "Jonas"},
    {"budget": 12, "director": "Gilberto"},
    {"budget": 13, "director": "Jhonata"}
]


def change_csv(csv, values_dict):
    for movie in csv.iterrows():
        csv["Budget"] = ""
        csv["Director"] = ""
        for values in values_dict:
            csv["Budget"] = [d['budget'] for d in data]
            csv["Director"] = [d['director'] for d in data]

    csv.to_csv("Movies_new.csv", index=False)
    return csv


change_csv(base, data)
print(base.head())
