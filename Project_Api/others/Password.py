import bcrypt
class Password:
    def __init__(self,password):
        self.password = password

    async def encript(self):    
        bytes = self.password.encode('utf-8')     
        password_encode =  bcrypt.hashpw(bytes, bcrypt.gensalt())
        return password_encode.decode('utf-8')
    
    async def compare(self,hash):
        return await bcrypt.checkpw(self.password,hash)