from db.conection import BDConexion
from db.conection import BDConexion

class DAOStudent:
    def list(self, student_id=None):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            if student_id:
                query = """SELECT s.id AS student_id, 
                                  s.name AS student_name, 
                                  s.paternal_surname, 
                                  s.maternal_surname,
                                  u.id AS user_id, 
                                  u.email, 
                                  u.avatar, 
                                  u.status,
                                  r.id AS role_id,
                                  r.name AS role_name
                           FROM student s
                           JOIN user u ON s.user_id = u.id
                           JOIN role r ON u.role_id = r.id
                           WHERE s.id = %s;"""
                cursor.execute(query, (student_id,))
            else:
                query = """SELECT s.id AS student_id, 
                                  s.name AS student_name, 
                                  s.paternal_surname, 
                                  s.maternal_surname,
                                  u.id AS user_id, 
                                  u.email, 
                                  u.avatar, 
                                  u.status,
                                  r.id AS role_id,
                                  r.name AS role_name
                           FROM student s
                           JOIN user u ON s.user_id = u.id
                           JOIN role r ON u.role_id = r.id;"""
                cursor.execute(query)
            
            rows = cursor.fetchall()
            for i in rows:
                data.append({
                    "id": i[0],
                    "maternal_surname": i[1],
                    "name": i[2],
                    "paternal_surname": i[3],
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

    def list_for_attendance(self, student_id=None):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()  # Elimina 'dictionary=True'
        try:
            if student_id:
                query = """SELECT s.id AS student_id,
                                s.name AS student_name,
                                s.paternal_surname,
                                s.maternal_surname,
                                se.name AS section_name,
                                c.name AS career_name,
                                u.avatar
                        FROM student s
                        JOIN section se ON s.section_id = se.id
                        JOIN career c ON se.career_id = c.id
                        JOIN user u ON s.user_id = u.id
                        WHERE s.id = %s;"""
                cursor.execute(query, (student_id,))
            else:
                query = """SELECT s.id AS student_id,
                                s.name AS student_name,
                                s.paternal_surname,
                                s.maternal_surname,
                                se.name AS section_name,
                                c.name AS career_name,
                                u.avatar
                        FROM student s
                        JOIN section se ON s.section_id = se.id
                        JOIN career c ON se.career_id = c.id
                        JOIN user u ON s.user_id = u.id;"""
                cursor.execute(query)

            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],  # Usar indexación por posición
                    "name": row[1],
                    "paternal_surname": row[2],
                    "maternal_surname": row[3],
                    "section_name": row[4],
                    "career_name": row[5],
                    "avatar": row[6]
                })
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()
