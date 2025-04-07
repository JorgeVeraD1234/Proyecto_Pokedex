from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.Factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
RM = ResponseManager()
pokemons_model = ModelFactory.get_model("pokemons")


@bp.route("/get/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    data = pokemons_model.find_by_id(ObjectId(pokemon_id))
    return RM.success(data)

@bp.route("/find_all", methods = ["GET"])
@jwt_required()
def find_all():
    try:
        data = pokemons_model.find_all()
        return data
    except ValidationError as err:
        return jsonify("Los pokemon estan muertos, chin no se ven ", 400)
