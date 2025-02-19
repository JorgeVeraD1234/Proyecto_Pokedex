from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.Factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemons_model = ModelFactory.get_model("pokemons")


@bp.route("/find_all", methods = ["GET"])
def find_all():
    try:
        data = pokemons_model.find_all()
        return data
    except ValidationError as err:
        return jsonify("Los pokemon estan muertos, chin no se ven ", 400)
    
    
@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemons_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)

