# courses/routes.py
from flask import Blueprint, jsonify, request\

from extensions import db
from courses.models import Course,Student,Enrollment,Department


courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

def make_response_json(data,status_code=200):
          return jsonify({'status':'success','data':data}),status_code


@courses_bp.route('/', methods=['GET'])
def get_courses():
          courses=db.session.scalars(db.select(Course)).all()
          serialized_courses=[course.to_dict() for course in courses]
          return make_response_json(serialized_courses)


@courses_bp.route('/', methods=['POST'])
def create_course():
          data =request.get_json()
          if not data:
                    return jsonify({"status":"error","message":"Invalid JSON or missing Content-Type header"}),400
          required_fields=['name','code','credits','department_id']
          missing_fields=[field for field in required_fields if field not in data]
          if(missing_fields):
                    return jsonify({"status":"error","message": f"Missing required fields:{', '.join(missing_fields)}"}),400
          
          new_course=Course(name=data['name'],code=data['code'],credits=data['credits'],department_id=data['department_id'])
          
          db.session.add(new_course)
          db.session.commit(),
          return make_response_json(new_course.to_dict(),201)

@courses_bp.route('/<int:course_id>/',methods=['GET'])
def get_course_detail(course_id):
          course=db.session.get(Course,course_id)
          if(course is None):
                    return jsonify({"starus":"error","message":"Course not found"}),404
          return make_response_json(course.to_dict())

@courses_bp.route('/<int:course_id>/',methods=['PUT'])
def update_course(course_id):
          course=Course.query.get_or_404(course_id)
          data=request.get_json() or {}
          
          course.name=data.get('name',course.name)
          course.code=data.get('code',course.code)
          course.credits=data.get('credits',course.credits)
          course.department_id=data.get('department_id',course.department_id)
          
          db.session.commit()
          return make_response_json(course.to_dict())

@courses_bp.route('/<int:course_id>/',methods=['DELETE'])
def delete_course(course_id):
          course=Course.query.get_or_404(course_id)
          db.session.delete(course)
          db.session.commit()
          return make_response_json({"message":f"Course {course_id} deleted successfully"})

@courses_bp.route('/<int:course_id>/students',methods=['GET'])
def get_enrolled_students(course_id):
          Course.query.get_or_404(course_id)
          
          enrolled_students=Student.query\
                    .join(Enrollment,Student.id==Enrollment.student_id)\
                    .filter(Enrollment.course_id==course_id)\
                    .all()
          
          serialized_students=[student.to_dict() for student in enrolled_students]
          return make_response_json(serialized_students)