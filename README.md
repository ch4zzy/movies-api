# Movie API
This API allows you to check list and detail of movies
The raw data was taken from the IMDb site using a [script](https://gitlab.com/ch4zzy/imdb-top250-parse).
## Endpoints

### List
```
GET /api/movies/: List all movies.
 - Title
 - Rating
 - Genres (id,title)
```
### Detail
```
GET /api/movies/{id}: Detail of movie.
 - Title
 - Release date
 - Rating
 - Genres (id, title)
 - Actors (id, name)
 - Similar movies (title, release date)
```
