# courses/routes.py
from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

mock_courses={
          1:{"id":1,"name":"Theory of Computation","code":"CS301","credits":4}
}

@courses_bp.route('/', methods=['GET'])
def get_courses():
          return jsonify(mock_courses)

def make_response_json(data,status_code=200):
          return jsonify({'status':'success','data':data}),status_code

@courses_bp.route('/', methods=['POST'])
def create_course():
          data =request.get_json()
          if not data:
                    return jsonify({"status":"error","message":"Invalid JSON or missing Content-Type header"}),400
          required_fields=['name','code','credits']
          missing_fields=[field for field in required_fields if field not in data]
          if(missing_fields):
                    return jsonify({"status":"error","message": f"Missing required fields:{", ".join(missing_fields)}"}),400
          
          new_id=max(mock_courses.keys(),default=0)+1
          new_course={
                    "id":new_id,"name":data['name'],"code":data['code'],"credits":data['credits']
          }
          mock_courses[new_id]=new_course
          return make_response_json(new_course,201)

@courses_bp.route('/<int:course_id>/',methods=['GET'])
def get_course_detail(course_id):
          course=mock_courses.get(course_id)
          if not course:
                    return jsonify({"status":"error","message":"Course not found"}),404
          return make_response_json(course)

@courses_bp.route('/<int:course_id>/',methods=['PUT'])
def update_course(course_id):
          if course_id not in mock_courses:
                    return jsonify({"status":"error","message":"Course not found"}),404
          
          data=request.get_json() or {}
          mock_courses[course_id].update({
                    "name":data.get("name",mock_courses[course_id]["name"]),
                    "code":data.get("code",mock_courses[course_id]["code"]),
                    "credits":data.get("credits",mock_courses[course_id]["credits"])
          })
          return make_response_json(mock_courses[course_id],200)

@courses_bp.route('/<int:course_id>/',methods=['Delete'])
def delete_course(course_id):
          if(course_id not in mock_courses):
                    return jsonify({"status":"error","message":"Course not found"}),404
          
          deleted_course=mock_courses.pop(course_id)
          return make_response_json({"message":f"Course {course_id} deleted successfully","course":deleted_course})