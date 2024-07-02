from flask import Flask ,jsonify,send_from_directory,Response,request
from prisma import Prisma
from flask_cors import CORS
from functions.face_detector import Face
import os
import datetime
#Creación de la aplicación en flask
app = Flask(__name__,static_folder='uploads')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Creación de la ruta ping
@app.route("/")
def home():
    return "Server listening"

#Creación de la ruta users
@app.route("/users")
async def users():
    prisma = Prisma()
    await prisma.connect()
    users_response = await prisma.user.find_many()
    users_data = [
        {
            "id":user.id,
            "email":user.email,
            "password":user.password,
            "name":user.name,
            "profile_picture_url":os.environ.get("API_URL")  +"/"+ user.profile_picture_url,
            "paternal_surname":user.paternal_surname,
            "maternal_surname":user.maternal_surname,
            "status":user.status
        }for user in users_response
    ]
    await prisma.disconnect()
    return jsonify(users_data)

@app.route("/user/<int:user_id>", methods=["DELETE"])
async def delete_user(user_id):
    prisma = Prisma()
    await prisma.connect()
    await prisma.user.delete(
        where={"id": user_id}
    )
    await prisma.disconnect()
    return '', 204

#Creación de la ruta departments
@app.route("/departments")
async def departments():
    prisma = Prisma()
    await prisma.connect()
    department_response = await prisma.department.find_many()
    departments_data = [
        {
            "id":department.id,
            "name":department.name

        }for department in department_response
    ]
    await prisma.disconnect()
    return jsonify(departments_data)

@app.route("/department", methods=["POST"])
async def create_department():
    data = request.json
    prisma = Prisma()
    await prisma.connect()
    new_department = await prisma.department.create(
        data={
            "name": data["name"]
        }
    )
    await prisma.disconnect()
    return jsonify({"id": new_department.id, "name": new_department.name}), 201

@app.route("/department/<int:department_id>", methods=["PUT"])
async def update_department(department_id):
    data = request.json
    prisma = Prisma()
    await prisma.connect()
    updated_department = await prisma.department.update(
        where={"id": department_id},
        data={
            "name": data["name"]
        }
    )
    await prisma.disconnect()
    return jsonify({"id": updated_department.id, "name": updated_department.name})

@app.route("/department/<int:department_id>", methods=["DELETE"])
async def delete_department(department_id):
    prisma = Prisma()
    await prisma.connect()
    await prisma.department.delete(
        where={"id": department_id}
    )
    await prisma.disconnect()
    return '', 204


#Creación de la ruta positions
@app.route("/positions")
async def positions():
    prisma = Prisma()
    await prisma.connect()
    position_response = await prisma.position.find_many()
    positions_data = [
        {
            "id":position.id,
            "name":position.name

        }for position in position_response
    ]
    await prisma.disconnect()
    return jsonify(positions_data)

@app.route("/position", methods=["POST"])
async def create_position():
    data = request.json
    prisma = Prisma()
    await prisma.connect()
    new_position = await prisma.position.create(
        data={
            "name": data["name"]
        }
    )
    await prisma.disconnect()
    return jsonify({"id": new_position.id, "name": new_position.name}), 201

@app.route("/position/<int:position_id>", methods=["PUT"])
async def update_position(position_id):
    data = request.json
    prisma = Prisma()
    await prisma.connect()
    updated_position = await prisma.position.update(
        where={"id": position_id},
        data={
            "name": data["name"]
        }
    )
    await prisma.disconnect()
    return jsonify({"id": updated_position.id, "name": updated_position.name})

@app.route("/position/<int:position_id>", methods=["DELETE"])
async def delete_position(position_id):
    prisma = Prisma()
    await prisma.connect()
    await prisma.position.delete(
        where={"id": position_id}
    )
    await prisma.disconnect()
    return '', 204

#Creación de la ruta roles
@app.route("/roles")
async def roles():
    prisma = Prisma()
    await prisma.connect()
    role_response = await prisma.role.find_many()
    roles_data = [
        {
            "id":role.id,
            "name":role.name

        }for role in role_response
    ]
    await prisma.disconnect()
    return jsonify(roles_data)

#Creación de la ruta registros
@app.route('/registers')
async def registers():
    prisma = Prisma()
    await prisma.connect()
    register_response = await prisma.register.find_many(include={"user":{"include":{"department":True,"position":True}}})
    registers_data = [
        {
            "id":register.id,
            "user_id":register.user_id,
            "date":register.date,
            "user": {
                "email":register.user.email,
                "name":register.user.name,
                "profile_picture_url":os.environ.get("API_URL") + "/" + register.user.profile_picture_url,
                "paternal_surname":register.user.paternal_surname,
                "maternal_surname":register.user.maternal_surname,
                "department": {
                    "id":register.user.department.id,
                    "name":register.user.department.name
                },
                "position": {
                    "id":register.user.position.id,
                    "name":register.user.position.name
                }
            }
        }for register in register_response
    ]
    await prisma.disconnect()
    return jsonify(registers_data)

@app.route("/register/<int:register_id>", methods=["DELETE"])
async def delete_register(register_id):
    prisma = Prisma()
    await prisma.connect()
    await prisma.register.delete(
        where={"id": register_id}
    )
    await prisma.disconnect()
    return '', 204

@app.route('/video_feed')
async def video_feed():
    prisma = Prisma()
    await prisma.connect()

    users_response = await prisma.user.find_many(include={"department":True,"position":True})
    users_data = []
    for user in users_response:
        exist = await prisma.register.find_first(where={"user_id":user.id})
        if not exist:
            print("No exist")
            users_data.append({
                "id":user.id,
                "email":user.email,
                "password":user.password,
                "name":user.name,
                "profile_picture_url":user.profile_picture_url,
                "paternal_surname":user.paternal_surname,
                "maternal_surname":user.maternal_surname,
                "status":user.status,
                "department": {
                    "id":user.department.id,
                    "name":user.department.name
                },
                "position": {
                    "id":user.position.id,
                    "name":user.position.name
                }
            }
            )
    await prisma.disconnect()
    return Response(Face.face_detector(users_data),
      mimetype="multipart/x-mixed-replace; boundary=frame")

#Ruta para ejecutar el script
@app.route('/runScript')
async def runScript():
    prisma = Prisma()
    await prisma.connect()
    #Creación de los roles
    if await prisma.role.count()==0:
        await prisma.role.create_many(data=[
            {"id":1,"name":"user"},
            {"id":2,"name":"admin"}
        ])
    # Creación de las cargos
    if await prisma.position.count()==0:
        await prisma.position.create_many(data=[
            {"id":1,"name":"Profesor"},
            {"id":2,"name":"Estudiante"}
        ])
    # Creación de los departmentos
    if await prisma.department.count()==0:
        await prisma.department.create_many(data=[
            {"id":1,"name":"Tecnología Digital"},
            {"id":2,"name":"Quimica y Minería"},
            {"id":3,"name":"Mecanica y Aviacíón"},
            {"id":4,"name":"Electronica y Electrecidad"},
            {"id":5,"name":"Diseño y producción Industrial"}
        ])
    # Creacion de los usuarios
    if await prisma.user.count()==0:
        await prisma.user.create_many(data = [
                {"id": 1, "email": "duberly.mondragon@tecsup.edu.pe", "password": "Duberly##**2004", "profile_picture_url": "uploads/duberly-ivan-mondragon-manchay.png", "name": "Duberly Ivan", "paternal_surname": "Mondragón", "maternal_surname": "Manchay", "role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 2, "email": "ethan.arredondo@tecsup.edu.pe", "password": "Ethan##**2004", "profile_picture_url": "uploads/ethan-sebastian-arredondo-yarihuaman.png", "name": "Ethan Sebastian", "paternal_surname": "Arredondo", "maternal_surname": "Yarihuaman", "role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 3, "email": "jesus.aguero@tecsup.edu.pe", "password": "Jesus##**2005", "profile_picture_url": "uploads/jesus-aguero-anchivilca.png", "name": "Jesus", "paternal_surname": "Aguero", "maternal_surname": "Anchivilca","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 4, "email": "jose.arcos@tecsup.edu.pe", "password": "Jose##**2003", "profile_picture_url": "uploads/jose-arcos-tejeda.png", "name": "Jose", "paternal_surname": "Arcos", "maternal_surname": "Tejeda","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 6, "email": "freddy.balboa@tecsup.edu.pe", "password": "Freddy##**2001", "profile_picture_url": "uploads/freddy-balboa-fuentes.png", "name": "Freddy", "paternal_surname": "Balboa", "maternal_surname": "Fuentes","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 7, "email": "david.balboa@tecsup.edu.pe", "password": "David##**2003", "profile_picture_url": "uploads/david-balboa-mercado.png", "name": "David", "paternal_surname": "Balboa", "maternal_surname": "Mercado","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 8, "email": "jeremy.bellido@tecsup.edu.pe", "password": "Jeremy##**2001", "profile_picture_url": "uploads/jeremy-bellido-nanez.png", "name": "Jeremy", "paternal_surname": "Bellido", "maternal_surname": "Nañez","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 9, "email": "sebastian.beteta@tecsup.edu.pe", "password": "Sebastian##**2003", "profile_picture_url": "uploads/sebastian-beteta-adauco.png", "name": "Sebastian", "paternal_surname": "Beteta", "maternal_surname": "Adauco","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 10, "email": "carlos.cabrera.r@tecsup.edu.pe", "password": "Carlos##**2004", "profile_picture_url": "uploads/carlos-cabrera-ricalde.png", "name": "Carlos", "paternal_surname": "Cabrera", "maternal_surname": "Ricalde","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 11, "email": "bruno.chigne@tecsup.edu.pe", "password": "Bruno##**2000", "profile_picture_url": "uploads/bruno-chigne-medina.png", "name": "Bruno", "paternal_surname": "Chigne", "maternal_surname": "Medina","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 12, "email": "jhon.churivanti@tecsup.edu.pe", "password": "Jhon##**2001", "profile_picture_url": "uploads/jhon-churivanti-alva.png", "name": "Jhon", "paternal_surname": "Churivanti", "maternal_surname": "Alva","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 13, "email": "max.cirineo@tecsup.edu.pe", "password": "Max##**2001", "profile_picture_url": "uploads/max-cirineo-alvarez.png", "name": "Max", "paternal_surname": "Cirineo", "maternal_surname": "Alvarez","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 14, "email": "adrian.coronel@tecsup.edu.pe", "password": "Adrian##**2001", "profile_picture_url": "uploads/adrian-coronel-mendoza.png", "name": "Adrian", "paternal_surname": "Coronel", "maternal_surname": "Mendoza","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 15, "email": "alvaro.cuba@tecsup.edu.pe", "password": "Alvaro##**2003", "profile_picture_url": "uploads/alvaro-cuba-porras.png", "name": "Alvaro", "paternal_surname": "Cuba", "maternal_surname": "Porras","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 16, "email": "harold.cutti@tecsup.edu.pe", "password": "Harold##**2005", "profile_picture_url": "uploads/harold-cutti-salazar.png", "name": "Harold", "paternal_surname": "Cutti", "maternal_surname": "Salazar","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 17, "email": "cielo.espinoza@tecsup.edu.pe", "password": "Cielo##**2002", "profile_picture_url": "uploads/cielo-espinoza-cortez.png", "name": "Cielo", "paternal_surname": "Espinoza", "maternal_surname": "Cortez","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 18, "email": "jared.garcia@tecsup.edu.pe", "password": "Jared##**2000", "profile_picture_url": "uploads/jared-garcia-borja.png", "name": "Jared", "paternal_surname": "Garcia", "maternal_surname": "Borja","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 19, "email": "antonio.guzman@tecsup.edu.pe", "password": "Antonio##**2001", "profile_picture_url": "uploads/antonio-guzman-giron.png", "name": "Antonio", "paternal_surname": "Guzman", "maternal_surname": "Giron","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 20, "email": "pedro.hernandez@tecsup.edu.pe", "password": "Pedro##**2000", "profile_picture_url": "uploads/pedro-hernandez-carhuajulca.png", "name": "Pedro", "paternal_surname": "Hernandez", "maternal_surname": "Carhuajulca","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 21, "email": "edilson.huaman@tecsup.edu.pe", "password": "Edilson##**2004", "profile_picture_url": "uploads/edilson-huaman-huanca.png", "name": "Edilson", "paternal_surname": "Huaman", "maternal_surname": "Huanca","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 23, "email": "william.postillos@tecsup.edu.pe", "password": "William##**2002", "profile_picture_url": "uploads/william-postillos-aquino.png", "name": "William", "paternal_surname": "Postillos", "maternal_surname": "Aquino","role_id": 1, "position_id": 2, "department_id": 1},
                {"id": 24, "email": "renzo.remuzgo@tecsup.edu.pe", "password": "Renzo##**2000", "profile_picture_url": "uploads/renzo-remuzgo-davila.png", "name": "Renzo", "paternal_surname": "Remuzgo", "maternal_surname": "Dávila","role_id": 1, "position_id": 2, "department_id": 1}])
        await prisma.disconnect()
    return "ok"

#Ruta para obtener los datos del script
@app.route('/getScript')
async def getScript():
    prisma = Prisma()
    await prisma.connect()
    roles_response = await prisma.role.find_many()
    position_response = await prisma.position.find_many()
    department_response = await prisma.department.find_many()
    users_response = await prisma.user.find_many()
    roles_data = [
        {
            "id":role.id,
            "name":role.name

        }for role in roles_response
    ]
    positions_data = [
        {
            "id":position.id,
            "name":position.name

        }for position in position_response
    ]
    departments_data = [
        {
            "id":department.id,
            "name":department.name

        }for department in department_response
    ]
    users_data = [
        {
            "id":user.id,
            "email":user.email,
            "name":user.name,
            "profile_picture_url":os.environ.get("API_URL") + "/" + user.profile_picture_url,
            "paternal_surname":user.paternal_surname,
            "maternal_surname":user.maternal_surname,
            "status":user.status
        }for user in users_response
    ]

    data = {
        "roles":roles_data,
        "postitions":positions_data,
        "departmens":departments_data,
        "users":users_data,
    }
    await prisma.disconnect()
    return jsonify(data)
    
#Ruta para eliminar los datos del script
@app.route('/deleteScript')
async def deleteScript():
    prisma = Prisma()
    await prisma.connect()
    #Eliminamos las tablas
    await prisma.register.delete_many()
    await prisma.user.delete_many()
    await prisma.role.delete_many()
    await prisma.position.delete_many()
    await prisma.department.delete_many()
    await prisma.disconnect()
    return "ok"

@app.route('/uploads/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == '__main__':
    app.run(debug=False)