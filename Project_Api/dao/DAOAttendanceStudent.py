from db.conection import BDConexion
class DAOAttendanceStudent:
    def list(self, attendance_id):
        data = []
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            query = """
                SELECT 
                    attendance_student.id,
                    attendance_student.attendance_id,
                    attendance_student.student_id,
                    attendance_student.date,
                    attendance_student.status,
                    student.paternal_surname,
                    student.maternal_surname,
                    student.name,
                    user.avatar
                FROM attendance_student
                JOIN student ON attendance_student.student_id = student.id
                JOIN user ON student.user_id = user.id
                WHERE attendance_student.attendance_id = %s
            """
            cursor.execute(query, (attendance_id,))
            rows = cursor.fetchall()
            for row in rows:
                data.append({
                    "id": row[0],
                    "attendance_id": row[1],
                    "student_id": row[2],
                    "date": row[3],
                    "status": row[4],
                    "paternal_surname": row[5],
                    "maternal_surname": row[6],
                    "name": row[7],
                    "avatar": row[8]
                })
            return data
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return False
        finally:
            con.close()

    def create(self,attendance_id, student_id,date,status):
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("""INSERT INTO attendance_student (attendance_id,student_id,date, status)
                            VALUES (%s, %s, %s, %s)""", (attendance_id,student_id,date,status))
            con.commit()
            return cursor.lastrowid  # Devolver el ID del último registro insertado
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return None  # Devolver None en caso de error
        finally:
            con.close()
    
    def exists(self, attendance_id, student_id):
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            # Consulta SQL para verificar si existe la asistencia para la fecha proporcionada
            cursor.execute("""SELECT COUNT(*) FROM attendance_student
                              WHERE attendance_id = %s AND student_id = %s""",
                           (attendance_id, student_id))
            
            # Obtener el resultado de la consulta
            row = cursor.fetchone()
            
            # Devolver True si hay al menos una fila, indicando que existe una asistencia para esa fecha
            return row[0] > 0
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            con.close()