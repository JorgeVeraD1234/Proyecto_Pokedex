#Cea
#Actualiza todos
#elimina
#Identificar la clase del modelo y evitar que se usen metodos indebidos


from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorite_schema import PokemonFavoritesSchema
from marshmallow import ValidationError
from app.models.Factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite")
pokemon_favorite_schema = PokemonFavoritesSchema()
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorite")

@bp.route("/add", methods = ["POST"])
def add_pokemon_favorite(pokemon_id):
    try:
        data = pokemon_favorite_schema.load(request.json)
        pokemon_favorite = pokemon_favorite_model.update(ObjectId(pokemon_id), data)
        return jsonify({
            "data": pokemon_favorite
        }, 200)        
    except ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    
@bp.route("/delete/<string:pokemon_id>", methods=["GET"])
def remove_pokemon_favorite(pokemon_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_id))
    return jsonify ("El pokemon ha sido eliminado de favoritos con exito", 200)
    
@bp.route("/find_all", methods = ["GET"])
def find_all():
    try:
        data = pokemon_favorite_model.find_all()
        return data
    except ValidationError as err:
        return jsonify("Los pokemon estan muertos, chin no se ven ", 400)
    
@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_favorite_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)

