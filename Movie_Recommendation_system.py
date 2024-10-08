# here i am creating a movies list with title and genre
movies = [
    {"title": "pushpha", "genre": "Action"},
    {"title": "kgf", "genre": "Action"},
    {"title": "Ranghsthalam", "genre": "Drama"},
    {"title": "Amma-bomma", "genre": "Horror"},
    {"title": "devara", "genre": "Action"},
    {"title": "Super", "genre": "Romance"},
    {"title": "jathirathnalu", "genre": "Comedy"},
    {"title": "Harrypotter", "genre": "Fantasy"},
    {"title": "The Witcher", "genre": "Fantasy"},
    {"title": "Dora", "genre": "Animation"}
]

# here Dictionary mapping users to their preferred genres
user_preference = {
    "Vijay Kumar": {"Action", "Romance"},
    "Ramesh Kumar": {"Drama", "Horror"},
    "Vijayalaxmi": {"Action", "Drama"},
    "Durga": {"Drama", "Horror"},
    "Ramukumar": {"Animation", "Comedy"}
}
# defining a function with operations to be performed 
def Movie_recommend_project():
    try:
        #taking input form user for  name and changing it to title 
        user_input = input("Enter user Name: ").strip().title()

        # Checking if the user exists in the preferences
        if user_input not in user_preference:
            print(f"User {user_input} is not in the preference list")
            return
        
        # Getting  the user's preferred genres
        preferred_genre = user_preference[user_input]

        # here storing  unique movie recommendations
        recommendations_movies = set()

        # Iterating  through the movie list and recommend movies that match the user's preferred genres
        for movie in movies:
            if movie["genre"] in preferred_genre:
                recommendations_movies.add(movie["title"])

        # printing movie recommendations 
        if recommendations_movies:
            print(f"{user_input}'s recommended movies are: {', '.join(recommendations_movies)}")
        else:
            print(f"No preferred movies found for {user_input}")
    #else exception will be handled 
    except Exception as e:
        print(f"An error occurred: {e}")

# looping untill the user wants to exit 
while True:
    Movie_recommend_project()
    # if user want to exit this block will execute
    continue_input = input("To continue for movie recommendations, enter YES. To exit, enter NO: ").strip().upper()
    if continue_input != 'YES':
        break
