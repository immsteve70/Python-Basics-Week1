movies = ["Inception", "Interstellar", "The Matrix", "Dune", "Oppenheimer"]

new_movie = input("Enter your fav movie: ")

movies.append(new_movie)

for num, movie in enumerate(movies, 1):
    print(f"{num}. {movie}")