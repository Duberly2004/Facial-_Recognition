from prisma import Prisma
from others.Messages import error_invalid_credentials
from others.Password import Password
from others.Token import Token
import datetime

class AuthController:
    prisma = Prisma()
    def __init__(self):
        pass

    async def login(self,request):
        data = request.get_json()
        await self.prisma.connect()
        email = data['email']
        password = data['password']

        user = await self.prisma.user.find_unique(where={"email":email})
        await self.prisma.disconnect()
        if user is None: return error_invalid_credentials,400

        password = Password(password)
        is_match = password.compare(user.password)

        if is_match == False: return error_invalid_credentials,400 
        token = Token()
        payload={"id":str(user.id),"email":user.email}
        access_token=token.generate(payload=payload)
        refresh_token=token.generate(payload=payload)

        return {"access_token":access_token,"refresh_token":refresh_token}