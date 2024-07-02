from db.conection import BDConexion
class DAOARegister:
    def create(self,user_id):
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("""INSERT INTO Register (user_id) VALUES (%s)""", (user_id))
            con.commit()
            return cursor.lastrowid  # Devolver el ID del último registro insertado
        except Exception as e:
            con.rollback()
            print("Error:", e)
            return None  # Devolver None en caso de error
        finally:
            con.close()
    def exists(self,user_id):
        con = BDConexion.connect(self)
        cursor = con.cursor()
        try:
            # Consulta SQL para verificar si existe la asistencia para la fecha proporcionada
            cursor.execute("""SELECT COUNT(*) FROM Register
                              WHERE user_id = %s """,
                           (user_id))
            
            # Obtener el resultado de la consulta
            row = cursor.fetchone()
            
            # Devolver True si hay al menos una fila, indicando que existe una asistencia para esa fecha
            return row[0] > 0
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            con.close()