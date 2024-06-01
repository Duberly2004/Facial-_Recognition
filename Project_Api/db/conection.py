import pymysql
class BDConexion():
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="my-secret-pw",db="db_pre_tesis")
