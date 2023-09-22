from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True, cascade="all, delete-orphan")
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active,
            
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    eyes_color = db.Column(db.String(80), nullable=False)
    hair_color = db.Column(db.String(80), nullable=False)
    height = db.Column(db.String(80), nullable=False)
    favorites = db.relationship('Favorites', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eyes_color": self.eyes_color,
            "hair_color": self.hair_color,
            "height": self.height,

            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    diameter = db.Column(db.String(80), nullable=False)
    gravity = db.Column(db.String(80), nullable=False)
    population = db.Column(db.String(80), nullable=False)
    rotation_period = db.Column(db.String(80), nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,          
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "rotation_period": self.rotation_period,

            # do not serialize the password, its a security breach
        }

 
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,

            # do not serialize the password, its a security breach
        }