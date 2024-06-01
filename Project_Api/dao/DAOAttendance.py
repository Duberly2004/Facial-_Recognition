from db.conection import BDConexion
class DAOAttendance:
    def list(self,section_id,course_id,id=None):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            if id is not None:
                cursor.execute(f"SELECT * FROM attendance WHERE course_id={course_id} AND section_id={section_id} AND id={id}")                
            else:
                cursor.execute(f"SELECT * FROM attendance WHERE course_id={course_id} AND section_id={section_id}")
            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],
                    "date": row[1],
                    "career_id":row[2],
                    "section_id":row[3],
                    "course_id":row[4]    
                    })
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()

    def create(self, date, career_id, section_id, course_id):
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("""INSERT INTO attendance (date, career_id, section_id, course_id)
                            VALUES (%s, %s, %s, %s)""", (date, career_id, section_id, course_id))
            con.commit()
            return cursor.lastrowid  # Devolver el ID del último registro insertado
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return None  # Devolver None en caso de error
        finally:
            con.close()
    
    def listForId(self,id):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(f"SELECT * FROM attendance WHERE id={id}")                
            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],
                    "date": row[1],
                    "career_id":row[2],
                    "section_id":row[3],
                    "course_id":row[4]    
                    })
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()