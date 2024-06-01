from flask import Flask,request,abort,send_from_directory
from flask_cors import CORS, cross_origin
from flask import Response
from functions.face_detector import Face
from dao.DAOStudent import DAOStudent
from dao.DAOTeacher import DAOTeacher
from dao.DAOCareer import DAOCareer
from dao.DAOSection import DAOSection
from dao.DAOCourse import DAOCourse
from dao.DAOAttendance import DAOAttendance
from dao.DAOAttendanceStudent import DAOAttendanceStudent
app = Flask(__name__,static_folder='images')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

#---------Student routes------------
@app.route('/students')
def students_list():
    users = DAOStudent.list(None)
    if(users): return users
    return []

#---------Student routes------------
@app.route('/teachers')
def teachers_list():
    teachers = DAOTeacher.list(None)
    if(teachers): return teachers
    return []

#---------Career routes------------
@app.route('/careers')
def careers_list():
    careers = DAOCareer.list(None)
    if(careers): return careers
    return []

#---------Section routes------------
@app.route('/career/<career_id>/sections')
def sections_list(career_id):
    sections = DAOSection.list(None,career_id)
    if(sections): return sections
    return []

#---------Course routes------------
@app.route('/career/<career_id>/courses')
def courses_list(career_id):
    courses = DAOCourse.list(None,career_id)
    if(courses): return courses
    return []

@app.route('/career/<career_id>/course/<id>/')
def course_list(career_id,id):
    course = DAOCourse.list(None,career_id,id)
    if(course): return course[0]
    return "not found", 404

#---------Attendance routes------------
@app.route('/section/<section_id>/course/<course_id>/attendances')
def attendances_list(section_id,course_id):
    attendances = DAOAttendance.list(None,section_id,course_id)
    if(attendances): return attendances
    return []

@app.route('/attendance/<id>')
def attendance_list(id):
    attendance = DAOAttendance.listForId(None,id)
    if(attendance): return attendance[0]
    return "not found", 404

@app.route('/attendance', methods=['POST'])
def create_attendance():
    data = request.get_json()
    try:
        if 'section_id' in  data and 'date' in data and 'section_id' in data and 'course_id' in data and 'career_id' in data:
            id = DAOAttendance().create(data["date"],data["career_id"],data["section_id"],data["course_id"])
            return {"id":id}  
        else : return 'Data is required', 400
    except Exception as e:
        abort(500, f"Error al crear la asistencia: {str(e)}")


#Attendance Student
@app.route('/attendances/<id_attendance>/attendancesStudents')
def attendances_stundent_list(id_attendance):
    attendances_stundent = DAOAttendanceStudent.list(None,id_attendance)
    if(attendances_stundent): return attendances_stundent
    return []

@app.route('/video_feed/<attendance_id>')
def video_feed(attendance_id):
    return Response(Face.face_detector(attendance_id),
      mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/images/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run()