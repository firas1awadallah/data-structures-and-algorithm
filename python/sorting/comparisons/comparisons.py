class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_year(movies):
    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            if movies[i].year < movies[j].year:
                movies[i], movies[j] = movies[j], movies[i]
    return movies

def sort_alphabet(movies):
    def get_sort_title(movie):
        title = movie.title.lower()
        if title.startswith(("a ", "an ", "the ")):
            return title[2:]
        return title
    
    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            if get_sort_title(movies[i]) > get_sort_title(movies[j]):
                movies[i], movies[j] = movies[j], movies[i]
    return movies


def compare_years(a, b):
    return b.year - a.year

def compare_titles(a, b):
    sort_a = a.title.lower()
    sort_b = b.title.lower()
    if sort_a.startswith(("a ", "an ", "the ")):
        sort_a = sort_a[2:]
    if sort_b.startswith(("a ", "an ", "the ")):
        sort_b = sort_b[2:]
    if sort_a > sort_b:
        return 1
    elif sort_a < sort_b:
        return -1
    else:
        return 0


movies = [
    Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
    Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
    Movie("The Shawshank Redemption", 1994, ["Drama"]),
    Movie("Fight Club", 1999, ["Drama"]),
]

sorted_by_year = sort_year(movies)
for movie in sorted_by_year:
    print(f"{movie.title} ({movie.year})")

print()


sorted_alphabetically = sort_alphabet(movies)
for movie in sorted_alphabetically:
    print(movie.title)

