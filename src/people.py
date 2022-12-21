from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema


def read_all():
    people = Person.query.all()
    # people variable contains a list of database items
    # serialize with dump
    return people_schema.dump(people)


def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def create(person):
    lname = person.get("lname")
    exisiting_person = Person.query.filter(Person.lname == lname).one_or_none()

    if exisiting_person is None:
        # load: deserialize data to internal representation
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")


def update(lname, person):
    exisitng_person = Person.query.filter(Person.lname == lname).one_or_none()
    
    if exisitng_person:
        update_person = person_schema.load(person, session=db.session)
        exisitng_person.fname = update_person.fname
        db.session.merge(exisitng_person)
        db.session.commit()
        return person_schema.dump(exisitng_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")


def delete(lname):
    exisitng_person = Person.query.filter(Person.lname == lname).one_or_none()
    
    if exisitng_person:
        db.session.delete(exisitng_person)
        db.session.commit()
        return make_response(f"{lname} successfully delete", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
