from film_API import FilmApi
from film import Filmers


api = FilmApi()
film = api.get_film(1)
print(film.title)
print(film.characters)
print(film.vehicles)
print(film.starships)
print(film.species)