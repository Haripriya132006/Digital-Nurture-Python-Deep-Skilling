from extensions import db


class Department(db.Model):
          __tablename__='departments'
          
          id=db.Column(db.Integer,primary_key=True)
          name=db.Column(db.String(100),nullable=False,unique=True)
          head_of_dept=db.Column(db.String(100),nullable=False)
          budget=db.Column(db.Integer,nullable=False)
          
          courses=db.relationship('Course',backref='department',lazy=True)
          students=db.relationship('Student',backref='department',lazy=True)
          
          def to_dict(self):
                    return {
                    'id':self.id,
                    'name':self.name,
                    'head_of_dept':self.head_of_dept,
                    'budget':self.budget
          }
class Course(db.Model):
          __tablename__='courses'
          
          id=db.Column(db.Integer,primary_key=True)
          name=db.Column(db.String(100),nullable=False)
          code=db.Column(db.String(20),nullable=False,unique=True)
          credits=db.Column(db.Integer,nullable=False)
          
          department_id=db.Column(db.Integer,db.ForeignKey('departments.id'),nullable=False)
          
          enrollments=db.relationship('Enrollment',backref='course',lazy=True)
          
          def to_dict(self):
                    return {
                              'id':self.id,
                              'name':self.name,
                              'code':self.code,
                              'credits':self.credits,
                              'department_id':self.department_id
                    }

class Student(db.Model):
          __tablename__='students'
          id=db.Column(db.Integer,primary_key=True)
          first_name=db.Column(db.String(50),nullable=False)
          last_name=db.Column(db.String(50),nullable=False)
          email=db.Column(db.String(120),nullable=False,unique=True)
          enrollment_year=db.Column(db.Integer,nullable=False)
          
          department_id=db.Column(db.Integer,db.ForeignKey('departments.id'),nullable=False)
          
          enrollments=db.relationship('Enrollment',backref='student',lazy=True)
          
          def to_dict(self):
                    return {
                              'id':self.id,
                              'first_name':self.first_name,
                              'last_name':self.last_name,
                              'email':self.email,
                              'enrollment_year':self.enrollment_year,
                              'department_id':self.department_id
                    }
                    
class Enrollment(db.Model):
          __tablename__='enrollments'
          id=db.Column(db.Integer,primary_key=True)
          enrollment_date=db.Column(db.DateTime,default=db.func.current_timestamp())
          grade=db.Column(db.String(2),nullable=True)
          
          student_id=db.Column(db.Integer,db.ForeignKey('students.id'),nullable=False)
          course_id=db.Column(db.Integer,db.ForeignKey('courses.id'),nullable=False)