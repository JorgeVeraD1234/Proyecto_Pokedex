from app import mongo
from app.models.super_clase import SuperClass

class User(SuperClass):
    def __init__(self):
        super().__init__("users")
        
    def find_all(self):
        return NotImplementedError("No es posible obtener todos los usuarios")
    
    def get_by_email_password(self, email, password):
        user = self.collection.find_one({"email": email, "password": password})
        return user
        

    
    
    
    