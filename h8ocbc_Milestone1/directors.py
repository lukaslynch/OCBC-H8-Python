from flask import make_response, abort
from config import db
from models import Directors, Movies, DirectorsSchema

def read_all():
    # Create the list of directors from our data
    directors = Directors.query.order_by(db.desc(Directors.id)).limit(5)

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    return data

def read_one(director_id):
    # Get director by id
    directors = (
        Directors.query.filter(Directors.id == director_id)
        .outerjoin(Movies)
        .one_or_none()
    )

    if directors is not None:

        director_schema = DirectorsSchema()
        data = director_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for Id: {director_id}")

def create(directors):
    # Cek jika ada directors yg sama lalu akan dijalankan post jika director tidak ada yang sama
    # terdapat validasi director name tidak boleh kosong, jika kosong otomatis return 204 code status
    name = directors.get("name")
    existing_director = (
        Directors.query.filter(Directors.name == name)
        .one_or_none()
    )

    if name != "":

        if existing_director is None:
            schema = DirectorsSchema()
            new_director = schema.load(directors, session=db.session)

            db.session.add(new_director)
            db.session.commit()

            data = schema.dump(new_director)

            return data, 201
        else:
            abort(409, f"Director {name} exists already!!")

def update(director_id, directors):
    # update director, get the director requested
    update_director = Directors.query.filter(
        Directors.id == director_id
    ).one_or_none()

    if update_director is not None:

        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        update.id = update_director.id
        db.session.merge(update)
        db.session.commit()
        data = schema.dump(update_director)

        return data, 200

    else:
        abort(404, f"director not found for Id: {director_id}")

def delete(director_id):
    # Get the director requested
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"director {director_id} deleted", 200)

    else:
        abort(404, f"direcor not found for Id: {director_id}")

def get_by_gender(gender):
    # get director by gender
    # Build the initial query
    # directors = Directors.query.with_entities(Directors.uid, Directors.name, Directors.department).filter(
    #     Directors.gender == gender).limit(5).all()
    

    directors = Directors.query.order_by(db.desc(Directors.id)).filter(
        Directors.gender == gender).limit(5)

    # Did we find a director by gender?
    if directors is not None:

        # Serialize the data for the response
        director_schema = DirectorsSchema(many=True)
        data = director_schema.dump(directors)
        return data
    # Otherwise, nope, didn't find that director by gender
    else:
        abort(404, f"MASUKKAN GENDER YANG ADA DIDATABASE: {gender}")