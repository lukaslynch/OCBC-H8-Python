from flask import make_response, abort
from config import db
from models import Directors, Movies, MoviesSchema
import datetime

def read_all():
    # Create the list of movies from our data
    movies = Movies.query.order_by(db.desc(Movies.id)).limit(5)

    # Serialize the data for the response
    movie_schema = MoviesSchema(many=True)
    data = movie_schema.dump(movies)
    return data

def read_one(director_id, movie_id):
    #fetch 1 data berdasarkan parameter director id dan movie id
    movie = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    if movie is not None:
        movie_schema = MoviesSchema()
        data = movie_schema.dump(movie)
        return data

    else:
        abort(404, f"movie not found for Id: {movie_id} in Director Id: {director_id}")

def create(director_id, movies):
    """
    fungsi create movies dengan masukkan director id dan object movies, jika id director
    tidak ditemukan maka akan mereturn 404, terdapat validasi release date dan akan return 400 
    jika masukkan release date tidak sesuai format
    """
    directors = Directors.query.filter(
        Directors.id == director_id).one_or_none()

    if directors is None:
        abort(404, f"director not found for Id: {director_id}")

    try:  # validate input date
        inputDate = movies['release_date']
        year, month, day = inputDate.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        abort(400, f"MASUKKAN FORMAT TANGGAL YANG BENAR: {inputDate}")

    schema = MoviesSchema()
    new_movie = schema.load(movies, session=db.session)

    directors.movies.append(new_movie)
    db.session.commit()

    data = schema.dump(new_movie)

    return data, 201


def update(director_id, movie_id, movies):
    """
    update movies dengan parameter director_id, movie_id dan object movies
    release date harus sesuai format, ada validasi release date
    jika salah satu id movie / director ada yang salah akan return 404
    """
    update_movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )

    try:  # validasi release date
        inputDate = movies['release_date']
        year, month, day = inputDate.split('-')
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        abort(400, f"MASUKKAN FORMAT TANGGAL YANG BENAR: {inputDate}")

    if update_movies is not None:

        schema = MoviesSchema()
        update = schema.load(movies, session=db.session)

        update.director_id = update_movies.director_id
        update.id = update_movies.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_movies)

        return data, 200

    else:
        abort(404, f"Movie not found for Id: {movie_id} in director Id: {director_id}")


def delete(director_id, movie_id):
    """
    delete movies sesuai parameter director_id dan movie_id, jika salah satu id salah akan
    return 404
    """
    movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == movie_id)
        .one_or_none()
    )
    if movies is not None:
        db.session.delete(movies)
        db.session.commit()
        return make_response(
            "movies {movie_id} deleted".format(movie_id=movie_id), 200
        )

    else:
        abort(404, f"Movie not found for Id: {movie_id} with id director {director_id}")

def budgetMore(budget):
    """
    fungsi sorting by more budget, fetch semua data yang budgetnya lebih dari parameter, 
    menerima parameter budget sebagai input, return movie dan directors yang sesuai kriteria
    jika input tidak berupa integer akan mengembalikan 404
    """
    movie = (Movies.query.filter(
        Movies.budget >= budget).order_by(Movies.budget).limit(5))

    if movie is not None:
        director_schema = MoviesSchema(many=True)
        data = director_schema.dump(movie)
        return data

    else:
        abort(404, f"no data that are more than this budget : {budget}")
