from prisma import Prisma
from flask import jsonify
from others.Password import Password
from others.Functions import Functions
from others.Enums import ERole, EUserType
from others.Errors import error_exist 
class StudentController:
    prisma = Prisma()

    async def _init_(self):
        pass

    async def create(self,request):
        await self.prisma.connect()
        data = request.get_json()
        name = data['name']
        lastname = data['lastname']
        functions = Functions()
        email = functions.remove_acents(f'{name.split(" ")[0].lower()}.{lastname.split(" ")[0].lower()}@tecsup.edu.pe')
        user = await self.prisma.user.find_unique(where={"email":email})
        if user: return error_exist,400
        #Buscar rol
        role = await self.prisma.role.find_unique(where={"name":ERole.USER})
        if role is None : return 404
        user_type = await self.prisma.user_type.find_unique(where={"name":EUserType.STUDENT})
        if user_type is None : return 404

        code = functions.generate_ramdom_code()
        password_code = functions.generate_ramdom_code(8)
        password = Password(password_code)
        await self.prisma.student.create(data={
            "user":{
                "create": {
                        "name":name,
                        "lastname":lastname,
                        "email":email,
                        "password":await password.encript(),
                        "code":code,
                        "role_id":role.id,
                        "user_type_id":user_type.id
                        }
                    }
        })
        await self.prisma.disconnect()
        return jsonify({"email":email,"password":code})
    
    async def list(self):
        await self.prisma.connect()
        response = await self.prisma.student.find_many(include={"user":True})
        data = [
            {
                "id":item.id,
                "email":item.user.email,
                "fullname":f'{item.user.name} {item.user.lastname}',
                "code":item.user.code,
                "is_active":item.user.is_active,
                "photo_url":item.user.photo_url
                
            }for item in response 
        ]
        print(response)
        await self.prisma.disconnect()
        return jsonify(data)
    