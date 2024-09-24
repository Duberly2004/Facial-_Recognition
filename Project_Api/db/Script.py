from prisma import Prisma
class Script:
    prisma = Prisma()
    def __init__(self):
        pass

    async def run(self):
        await self.prisma.connect()
        await self.prisma.role.create_many(data=[
            {'id':1,"name":"user"},
            {'id':2,"name":"admin"},
        ])
        await self.prisma.user_type.create_many(data=[
            {"id":1,"name":"teacher"},
            {"id":2,"name":"student"},
        ])
        await self.prisma.cycle.create_many(data=[
            {"id":1,"name":"1"},
            {"id":2,"name":"2"},
            {"id":3,"name":"3"},
            {"id":4,"name":"4"},
            {"id":5,"name":"5"},
            {"id":6,"name":"6"},
            {"id":7,"name":"7"}
        ])
        await self.prisma.section.create_many(data=[
            {"id":1,"name":"A"},
            {"id":2,"name":"B"},
            {"id":3,"name":"C"},
            {"id":4,"name":"D"}
        ])
        await self.prisma.career.create_many(data=[
            {"id":1,"name":"Diseño y Desarrollo de Sofware","code":"115321"}
        ])
        await self.prisma.course.create_many(data=[
            {"id":1,"name":"Sociedad y Desarrollo Sostenible","code":"115322"},
            {"id":2,"name":"Emprendimiento","code":"115323"},
            {"id":3,"name":"Start up venture project","code":"115324"},
            {"id":4,"name":"Consultoria y Desarrollo Profesional","code":"115325"},
            {"id":5,"name":"Inteligencia de Negocios","code":"115326"},
            {"id":6,"name":"Desarrollo de Aplicaciones Empresariales Avanzado","code":"115327"},
            {"id":7,"name":"Integración de Sistemas Empresariales Avanzado","code":"115328"},
            {"id":8,"name":"Gestión de Servicio de Software","code":"115329"}
        ])
        
        await self.prisma.disconnect()

    async def delete(self):
        await self.prisma.connect()
        await self.prisma.role.delete_many()
        await self.prisma.user_type.delete_many()
        await self.prisma.course.delete_many()
        await self.prisma.cycle.delete_many()
        await self.prisma.career.delete_many()
        await self.prisma.section.delete_many()
        await self.prisma.disconnect()

    async def get(self):
        await self.prisma.connect()
        roles = [
            {
                "id":item.id,
                "name":item.name
            }for item in await self.prisma.role.find_many()
        ] 
        user_types = [
            {
                "id":item.id,
                "name":item.name
            }for item in await self.prisma.user_type.find_many()
        ]
        await self.prisma.disconnect()
        return {"roles":roles,"user_types":user_types}