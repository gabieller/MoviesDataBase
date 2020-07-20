import pandas as pd

df = pd.read_csv("Movies.csv")

for genre in genres:
    names.append(genre['name'])
    genre.replace("Science Fiction", "Sci-Fic")
#return "|".join(names) 

df.head(5)