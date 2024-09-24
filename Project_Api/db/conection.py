import pymysql
from prisma import Prisma
class BDConexion():
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="duberly2004",db="db_project")

prisma = Prisma()