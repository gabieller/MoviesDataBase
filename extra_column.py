import pandas as pd

base = pd.read_csv("Filmes2.csv")


def extra_column(csv):
    cont = []
    csv["Contagem"] = ""
    for n in reversed(range(len(csv))):
        cont.append(n)
    for movie in csv.iterrows():
        csv["Contagem"] = cont
    csv.to_csv("Filmes_new.csv", index=False)
    return csv


add_column(base)
print(base.head())
