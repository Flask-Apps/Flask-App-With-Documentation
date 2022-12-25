from datetime import datetime
from config import db, ma


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class Person(db.Model):
    # gives Person the SQLAlchemy features to connect
    # to the database and access its tables
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    # represent 1 to many relationship
    notes = db.relationship(
        Note,
        # create a backwards reference in Note objects.
        # each instance of Note will contain an attribute called .person
        # which reference the parent object that a particular Note
        # instance is associated with
        # this allows us to have parent information in child
        backref="person",
        # delete all the Note instances that are associated with this
        # person (associated one)
        cascade="all, delete. delete-orphan",
        # required if delete-orphan is part of cascade parameter
        # not allow an orphaned Note instance
        single_parent=True,
        # tell how to sort the Note instances associated with a Person
        # object.
        order_by="desc(Note.timestamp)",
    )


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        # we're able to deserialize JSON data and load Person model
        # instances from it
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
# expect an iterable to serialize
people_schema = PersonSchema(many=True)
