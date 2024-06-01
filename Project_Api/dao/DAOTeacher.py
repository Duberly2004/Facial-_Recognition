from db.conection import BDConexion
class DAOTeacher:
    def list(self):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("""SELECT t.id AS teacher_id, 
                                      t.name AS teacher_name, 
                                      t.paternal_surname, 
                                      t.maternal_surname,
                                      u.id AS user_id, 
                                      u.email, 
                                      u.avatar, 
                                      u.status,
                                      r.id AS role_id,
                                      r.name AS role_name
                               FROM teacher t
                               JOIN user u ON t.user_id = u.id
                               JOIN role r ON u.role_id = r.id;
                           """)
            rows = cursor.fetchall()
            for i in rows:
                data.append({
                    "id": i[0],
                    "teacher_name": i[1],
                    "paternal_surname": i[2],
                    "maternal_surname": i[3],
                    "user": {
                        "id": i[4],
                        "email": i[5],
                        "avatar": i[6],
                        "status": i[7]
                    },
                    "role": {
                        "id": i[8],
                        "name": i[9]
                    }
                })
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()
 