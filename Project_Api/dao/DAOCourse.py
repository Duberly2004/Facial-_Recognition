from db.conection import BDConexion
class DAOCourse:
    def list(self,career_id,id=None):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            if id is not None:
                cursor.execute(f"SELECT * FROM course WHERE career_id={career_id} AND id={id}")
            else:
                cursor.execute(f"SELECT * FROM course WHERE career_id={career_id}")
            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],
                    "name": row[1],
                    "career_id":row[2]
                    })

            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()
