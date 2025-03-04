from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorite_schema import PokemonFavoritesSchema
from marshmallow import ValidationError
from app.models.Factory import ModelFactory
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

RM = ResponseManager()
bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite")
FP_SCHEMA = PokemonFavoritesSchema()
FP_MODEL = ModelFactory.get_model("pokemon_favorite")



@bp.route("/", methods = ["POST"])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data= request.json
        data = FP_SCHEMA.load(data)
        data["user_id"] = user_id
        fp = FP_MODEL.create(data)
        return RM.success ({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar todos los parametros")
#Delete
@bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success("Pokemon eliminado con exito")
#GET ALL
@bp.route("/", methods = ["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)

