from flask import Flask ,jsonify,send_from_directory,Response,request
from prisma import Prisma,register
from flask_cors import CORS
from functions.face_detector import Face
from others.Enums import ERole, EUserType
from controllers.TeacherController import TeacherController
from controllers.StudentController import StudentController
from controllers.OtherController import OtherController
from controllers.AuthController import AuthController
from db.Script import Script
import os

app = Flask(__name__,static_folder='uploads')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Ping
@app.route("/")
def home():
    return "Server listening"

#user_types
@app.route(f'/{ERole.ADMIN}/user_types')
async def user_types():
    return await OtherController().user_types()

@app.route(f'/{ERole.ADMIN}/courses')
async def courses():
    return await OtherController().courses()

@app.route(f'/{ERole.ADMIN}/cycles')
async def cycles():
    return await OtherController().cycles()

@app.route(f'/{ERole.ADMIN}/careers')
async def careers():
    return await OtherController().careers()

@app.route(f'/{ERole.ADMIN}/sections')
async def sections():
    return await OtherController().sections()

#----Teachers---
@app.route(f'/{ERole.ADMIN}/teachers',methods=["GET","POST","DELETE"])
async def teachers():
    if request.method == "GET":
        return await TeacherController().list()
    if request.method == "POST":
        return await TeacherController().create(request=request)
    if request.method == "DELETE":
        return await TeacherController().delete()

#----Students---
@app.route(f'/{ERole.ADMIN}/students',methods=["GET","POST","DELETE"])
async def students():
    if request.method == "GET":
        return await StudentController().list()
    if request.method == "POST":
        return await StudentController().create(request=request)

#----Auth----
@app.route('/login')
async def login():
    return await AuthController().login(request=request)

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
    user = await prisma.user.find_unique(where={"id":user_id})
    os.remove(user.profile_picture_url)
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
@app.route('/run_script')
async def run_script():
    await Script().run()
    return "ok"

#Ruta para obtener los datos del script
@app.route('/get_script')
async def get_script():
    data = await Script().get()
    return jsonify(data)
    
#Ruta para eliminar los datos del script
@app.route('/delete_script')
async def delete_script():
    await Script().delete()
    return "ok"

@app.route('/uploads/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)