from movies import movies

def sublistOfMovies(movies):
    sublist = []
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            sublist.append(movies[i])
    
    return sublist

print(sublistOfMovies(movies))