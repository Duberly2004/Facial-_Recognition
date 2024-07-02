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

@app.route('/video_feed')
async def video_feed():
    prisma = Prisma()
    await prisma.connect()

    users_response = await prisma.user.find_many(include={"department":True,"position":True})
    users_data = []
    for user in users_response:
        exist = await prisma.register.find_first(where={"user_id":user.id})
        print(exist)
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
        await prisma.user.create_many(data=[
            {"id":1,"email":"duberly.mondragon@tecsup.edu.pe","password":"Duberly##**2004","profile_picture_url":"uploads/duberly-ivan-mondragon-manchay.png","name":"Duberly Ivan","paternal_surname":"Mondragón","maternal_surname":"Manchay","role_id":1,"position_id":2,"department_id":1},
            {"id":2,"email":"ethan.arredondo@tecsup.edu.pe","password":"Ethan##**2004","profile_picture_url":"uploads/ethan-sebastian-arredondo-yarihuaman.png","name":"Ethan Sebastian","paternal_surname":"Arredondo","maternal_surname":"Yarihuaman","role_id":1,"position_id":2,"department_id":1}
        ])

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