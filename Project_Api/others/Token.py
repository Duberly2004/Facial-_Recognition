import jwt
from others.Enviroments import SECRET_KEY
class Token:
    def __init__(self):
        pass

    def generate(self,payload):
        return jwt.encode(payload=payload,key=SECRET_KEY)
    
    def verify(self,token):
        return jwt.decode(token,key=SECRET_KEY)