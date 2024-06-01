import cv2
import face_recognition
import os
import datetime
from dao.DAOAttendanceStudent import DAOAttendanceStudent
from dao.DAOStudent import DAOStudent
from db_exel.exel import Exel
file_names =  os.listdir('images') #Lista de los nombres de las imagenes
students = DAOStudent().list_for_attendance()

#########################
cap = cv2.VideoCapture(0)
class Face:

    def face_detector(attendance_id):
        while True:
            ret,frame = cap.read()
            if ret==False:break
            frame = cv2.flip(frame,1)
            
            face_locations = face_recognition.face_locations(frame)
            if face_locations != []:
                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    face_frame_encodings = face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
                    for student in students:
                        image = cv2.imread(student['avatar'])
                        if image is not None:
                            face_loc = face_recognition.face_locations(image)[0]
                            face_image_encodings = face_recognition.face_encodings(image,known_face_locations=[face_loc])
                            result = face_recognition.compare_faces(face_frame_encodings,face_image_encodings)
                            if result[0] == True:
                                text = student['name']
                                color = (125,220,0)
                                exist = DAOAttendanceStudent().exists(attendance_id,student_id=student['id'])
                                if not exist:
                                    print("Registrado")
                                    Exel.registerAttendance([
                                        [
                                        student['name']+" "+student['paternal_surname']+" "+student['maternal_surname'],
                                        str(datetime.datetime.now()),
                                        student['section_name'],
                                        "PRESENT"]
                                    ])
                                    DAOAttendanceStudent().create(attendance_id=attendance_id, student_id=student['id'], date=datetime.datetime.now(), status="PRESENT")
                                else:
                                    break
                                break
                            else:
                                print("Persona desconocida")
                                text ="Desconocido"
                                color = (50,40,255)
                        else:
                            print("No se pudo ler la imagen")

                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)   # Borde del rectángulo en color rojo
                    # Agregar texto dentro del rectángulo
                    cv2.putText(frame, text, (left + 10, bottom + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            (flag,encodedImage) = cv2.imencode('.jpg',frame)
            if not flag:
                continue
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                bytearray(encodedImage) + b'\r\n')