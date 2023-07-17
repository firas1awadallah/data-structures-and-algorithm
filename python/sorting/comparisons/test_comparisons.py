import pytest

from comparisons import sort_year, sort_alphabet, compare_years, compare_titles, Movie

# Tests year
def test_sort_year():
    movies = [
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("Fight Club", 1999, ["Drama"]),
    ]
    sorted_movies = sort_year(movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2010, 2008, 1999, 1994, 1994]

# Tests alphabet
def test_ort_alphabet():
    movies = [
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("Fight Club", 1999, ["Drama"]),
    ]
    sorted_movies = sort_alphabet(movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == [ "The Dark Knight", "The Shawshank Redemption","Fight Club", "Inception", "Pulp Fiction"]

# Tests for comparator 
def test_compare_years():
    movie1 = Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"])
    movie2 = Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"])
    assert compare_years(movie1, movie2) > 0

def test_compare_titles():
    movie1 = Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"])
    movie2 = Movie("Inception", 2010, ["Action", "Adventure", "Sci-Fi"])
    assert compare_titles(movie1, movie2) < 0
