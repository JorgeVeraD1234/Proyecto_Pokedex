import bcrypt

class EncryptionManager:
    def create_hash(self, text):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(text.encode("utf-8"), salt).decode("utf-8")
    
    def compare_hashes(self, text, hashpaw):
        return bcrypt.checkpw(text.encode("utf-8"), hashpaw.encode("utf-8"))
    
    
    