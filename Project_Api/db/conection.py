import pymysql
class BDConexion():
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="duberly2004",db="db_pretesis")
