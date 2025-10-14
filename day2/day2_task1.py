movies = ["Inception", "Interstellar", "The Matrix", "Dune", "Oppenheimer"]

for movie, i in enumerate(movies, 1):
    print(f"{movie}. {i}")

new_movie = input("Enter your favourite movie: ")

movies.append(new_movie)

print("Updated movie list:")

for num, movie in enumerate(movies, 1):
    print(f"{num}. {movie}")