from db.conection import BDConexion
class DAOCareer:
    def list(self):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM career")
            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],
                    "name": row[1]
                    })

            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()
