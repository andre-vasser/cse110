movies = [] 

while True: 
    movie = input("Enter the name of the movies: ")
    if movie.lower() =="quit":
        break;
    movies.append (movie)


for i, item in enumerate(movies, 1):
    print(f"{i}-{item}")


while True:
    
    order_list = input("Do you want order the list? Y/N: ")
    if order_list.lower() == "y":
        movie_a = int(input("Enter the index the first movie do you want dto swap: "))-1
        movie_b = int(input("Enter the input of the second movie do you want to swap: "))-1
        movie_x = movies[movie_a]
        movies [movie_a] = movies [movie_b]
        movies [movie_b] = movie_x
    
    else:
        break;
    
for i, item in enumerate(movies, 1):
    print(f"{i}-{item}")
    
        