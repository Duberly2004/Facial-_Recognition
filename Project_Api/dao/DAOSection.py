from db.conection import BDConexion
class DAOSection:
    def list(self,career_id):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(f"SELECT * FROM section where career_id={career_id}")
            rows = cursor.fetchall()
            for i in rows:
                data.append({
                    "id": i[0],
                    "name": i[1]})
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()
