"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, PlanetFavorite, CharacterFavorite
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

#            USER 

@api.route('/users', methods=['POST','GET'])
def handle_user():
    if request.method == 'GET':
        users = User.query.all()
        users_dictionary = []
        for user in users:
            users_dictionary.append(user.serialize())
        return jsonify(users_dictionary), 200
    else:
        new_user_data = request.json
        try:
            new_user = User.create(**new_user_data)
            return jsonify(new_user.serialize()), 201
        except Exception as error:
            raise Exception(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/users/<int:position>', methods=["DELETE"])
def handle_user_delete(position):
    User.query.filter_by(id=position).delete()
    db.session.commit()
    return f"User {position} was deleted succesfully"

#            CHARACTER 

@api.route('/characters', methods=['POST','GET'])
def handle_character():
    if request.method == 'GET':
        characters = Character.query.all()
        characters_dictionary = []
        for character in characters:
            characters_dictionary.append(character.serialize())
            return jsonify(characters_dictionary), 200
    else:
        new_character_data = request.json
        try:
            new_character = Character.create(**new_character_data)
            return jsonify(new_character.serialize()), 201
        except Exception as error:
            raise Exception(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/characters/<int:position>', methods=["DELETE"])
def handle_character_delete(position):
    Character.query.filter_by(id=position).delete()
    db.session.commit()
    return f"Character {position} was deleted succesfully"

#            CHARACTER FAVORITE

@api.route('/characters/favorites', methods=['POST'])
def handle_character_favorite():
    new_character_favorite_data = request.json
    try:
        new_character_favorite = CharacterFavorite.create(**new_character_favorite_data)
        return jsonify(new_character_favorite.serialize()), 201
    except Exception as error:
            raise Exception(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/characters/favorites/<int:userid>', methods=['GET'])
def handle_character_favorite_get(userid):
    characters_favorite = CharacterFavorite.query.filter_by(user_id=userid)
    characters_favorite_dictionary = []
    for favorite in characters_favorite:
        characters_favorite_dictionary.append(favorite.serialize())
        return jsonify(characters_favorite_dictionary), 200

@api.route('/characters/favorites/<int:position>', methods=["DELETE"])
def handle_character_favorite_delete(position):
    CharacterFavorite.query.filter_by(id=position).delete()
    db.session.commit()
    return f"Character Favorite with ID {position} was deleted succesfully"


#            PLANET 

@api.route('/planets', methods=['POST','GET'])
def handle_planet():
    if request.method == 'GET':
        planets = Planet.query.all()
        planets_dictionary = []
        for planet in planets:
            planets_dictionary.append(planet.serialize())
            return jsonify(planets_dictionary), 200
    else:
        new_planet_data = request.json
        try:
            new_planet = Planet.create(**new_planet_data)
            return jsonify(new_planet.serialize()), 201
        except Exception as error:
            raise Exception(error.args[0], error.args[1] if len(error.args) > 1 else 500)

#            PLANET FAVORITE

@api.route('/planets/favorites', methods=['POST'])
def handle_planet_favorite():
    new_planet_favorite_data = request.json
    try:
        new_planet_favorite = PlanetFavorite.create(**new_planet_favorite_data)
        return jsonify(new_planet_favorite.serialize()), 201
    except Exception as error:
            raise Exception(error.args[0], error.args[1] if len(error.args) > 1 else 500)

@api.route('/planets/favorites/<int:userid>', methods=['GET'])
def handle_planet_favorite_get(userid):
    planets_favorite = PlanetFavorite.query.filter_by(user_id=userid)
    planets_favorite_dictionary = []
    for favorite in planets_favorite:
        planets_favorite_dictionary.append(favorite.serialize())
        return jsonify(planets_favorite_dictionary), 200

@api.route('/planets/favorites/<int:position>', methods=["DELETE"])
def handle_planet_favorite_delete(position):
    PlanetFavorite.query.filter_by(id=position).delete()
    db.session.commit()
    return f"Planet Favorite with ID {position} was deleted succesfully"