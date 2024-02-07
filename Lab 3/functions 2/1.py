from movies import movies

def hasHighScore(movie):
    if movie["imdb"] > 5.5:
        return True
    
    return False

x = int(input("Enter the movie number: "))
print(hasHighScore(movies[x-1]))