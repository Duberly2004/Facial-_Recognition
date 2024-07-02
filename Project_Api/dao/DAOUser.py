from prisma import Prisma
import os

class DAOUser:
    async def list(student_id=None):
        prisma = Prisma()
        await prisma.connect()
        users_response = await prisma.user.find_many()
        users_data = [
            {
                "id":user.id,
                "email":user.email,
                "password":user.password,
                "name":user.name,
                "profile_picture_url":os.environ.get("API_URL") + user.profile_picture_url,
                "paternal_surname":user.paternal_surname,
                "maternal_surname":user.maternal_surname,
                "status":user.status
            }for user in users_response
        ]
        await prisma.disconnect()
        return users_data
