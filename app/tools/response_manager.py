from flask import jsonify

class ResponseManager:
    def success(self, data):
        if isinstance(data, str):
            data = {
                "message": data
            }
        return jsonify(data), 200 #Todo good
    
    def error(self, data="Invalid request"):
        if isinstance(data, str):
            data = {
                "message": data
            }
        return jsonify(data), 400 #Su culpa
    
    def error_server(self, data="Server error"):
        if isinstance(data, str):
            data = {
                "message": data
            }
        return jsonify(data), 500 #Mi culpa
        
        