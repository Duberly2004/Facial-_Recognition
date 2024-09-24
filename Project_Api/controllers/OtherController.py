from flask import jsonify
from prisma import Prisma 
class OtherController:
    prisma = Prisma()
    
    def __init__(self):
        pass

    async def user_types(self):
        await self.prisma.connect()
        data = [{
                "id":item.id,
                "name":item.name
            } for item in await self.prisma.user_type.find_many()]
        await self.prisma.disconnect()
        return jsonify(data)
            
    async def courses(self):
        await self.prisma.connect()
        data = [{
                "id":item.id,
                "name":item.name
            } for item in await self.prisma.course.find_many()]
        await self.prisma.disconnect()
        return jsonify(data)

    async def careers(self):
        await self.prisma.connect()
        data = [{
                "id":item.id,
                "name":item.name
            } for item in await self.prisma.career.find_many()]
        await self.prisma.disconnect()
        return jsonify(data)

    async def cycles(self):
        await self.prisma.connect()
        data = [{
                "id":item.id,
                "name":item.name
            } for item in await self.prisma.cycle.find_many()]
        await self.prisma.disconnect()
        return jsonify(data)

    async def sections(self):
        await self.prisma.connect()
        data = [{
                "id":item.id,
                "name":item.name
            } for item in await self.prisma.section.find_many()]
        await self.prisma.disconnect()
        return jsonify(data)