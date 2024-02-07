from movies import movies

def myFunc(movies, user_category):
    for i in range(len(movies)):
        if movies[i]["category"] == user_category:
            print(movies[i]["name"])

user_category = input()
myFunc(movies, user_category)