import bcrypt
class Password:
    def __init__(self,password):
        self.password = password
    def encode(self,pass_encode):
        return pass_encode.encode('utf-8')
    
    def decode(self,pass_decode):
        return pass_decode.decode('utf-8')     

    def encript(self):    
        bytes = self.encode(self.password) 
        password_encode =  bcrypt.hashpw(bytes, bcrypt.gensalt())
        return self.decode(password_encode)
    
    def compare(self,hash):
        bytes_hash = self.encode(hash)
        bytes_password = self.encode(self.password)
        return bcrypt.checkpw(bytes_password,bytes_hash)