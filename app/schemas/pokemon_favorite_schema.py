from marshmallow import Schema, fields, ValidationError

class PokemonFavoritesSchema(Schema):
    
    id = fields.Str(
        required = True,
        validate = lambda x: len (x) > 0,
        error_messages={
            "required": "El id del pokemon es requerido"
        }
    )
    name = fields.Str(
        required=True,
        validate =lambda x: len (x)>0,
        error_messages={
            "required": "El nombre es requerido"
        }
    )
    
    id = fields.Str(
        required = True,
        validate = lambda x: len (x) > 0,
        error_messages={
            "required": "El id del usuaio es requerido"
        }
    )
    


##id, name and id user