from movies import movies

def avg_imdb_by_cat(movies, category):
    c = 0
    sum = 0
    for i in movies:
        if i['category'] == category:
            sum += i['imdb']
            c += 1
    return sum/c

category = input('Enter a category: ')
print(avg_imdb_by_cat(movies, category))