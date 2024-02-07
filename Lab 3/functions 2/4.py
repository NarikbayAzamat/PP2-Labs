from movies import movies

def avg_imdb(movies):
    amountOfMovies = len(movies)
    sum = 0
    for i in movies:
        sum += i['imdb']
    return sum/amountOfMovies

print(avg_imdb(movies))