import cv2
import face_recognition
import os
import datetime
from dao.DAORegister import DAOARegister
from db_exel.exel import Exel
file_names =  os.listdir('uploads') #Lista de los nombres de las imagenes

#########################
cap = cv2.VideoCapture(0)
class Face:

    def face_detector(users):
        print(users)
        while True:
            ret,frame = cap.read()
            if ret==False:break
            frame = cv2.flip(frame,1)
            
            face_locations = face_recognition.face_locations(frame)
            if face_locations != []:
                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    face_frame_encodings = face_recognition.face_encodings(frame,known_face_locations=[face_location])[0]
                    for user in users:
                        print(user["id"])
                        image = cv2.imread(user['profile_picture_url'])
                        if image is not None:
                            face_loc = face_recognition.face_locations(image)[0]
                            face_image_encodings = face_recognition.face_encodings(image,known_face_locations=[face_loc])
                            result = face_recognition.compare_faces(face_frame_encodings,face_image_encodings)
                            if result[0] == True:
                                text = user['name']
                                color = (125,220,0)
                                exist = DAOARegister().exists(user_id=user['id'])
                                if not exist:
                                    print("Registrado")
                                    Exel.registerAttendance([
                                        [
                                            user['name']+" "+ user['paternal_surname']+" "+ user['maternal_surname'],
                                            user['department']['name'],user['position']['name'],
                                            str(datetime.datetime.now())]
                                        ])
                                        #Registrar aquí
                                    DAOARegister.create(self=None,user_id=user["id"])
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