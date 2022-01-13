"""this handles all database communications"""
import datetime

from flask.scaffold import F
from rentalapp import db



class Post(db.Model):
    __tablename__ = 'landlord'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    landlord_name = db.Column(db.String(255),nullable=False)
    landlord_phone = db.Column(db.Text(),nullable=False)
    landlord_date = db.Column(db.DateTime(),default=datetime.datetime.utcnow)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    student_name = db.Column(db.String(255),nullable=False)
    student_phone = db.Column(db.Text(),nullable=False)
    student_email = db.Column(db.String(255),nullable=False)
    student_state = db.Column(db.String(255),nullable=False)
    student_matric = db.Column(db.Integer(),nullable=False)
    student_col = db.Column(db.String(255),nullable=False)
    student_date = db.Column(db.DateTime(),default=datetime.datetime.utcnow)


class Property(db.Model):
    __tablename__ = 'property'
    prop_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    prop_contact = db.Column(db.String(255),nullable=False)
    prop_phone = db.Column(db.String(255),nullable=False)
    prop_filename = db.Column(db.Integer(),nullable=False)
    prop_price = db.Column(db.Integer(),nullable=False)
    prop_name = db.Column(db.Integer(),nullable=False)
    prop_date = db.Column(db.DateTime(),default=datetime.datetime.utcnow)


class Duration(db.Model):
    __tablename__ = 'duration'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    landlord_id = db.Column(db.Integer(),nullable=False)
    duration_date = db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    duration = db.Column(db.Integer(),nullable=False)
    number_of_student = db.Column(db.Integer(),nullable=False)
    location = db.Column(db.String(255),nullable=False)
    property_name = db.Column(db.String(255),nullable=False)
    student_id = db.Column(db.Integer(),db.ForeignKey('student.id'))
    property_id = db.Column(db.Integer(),db.ForeignKey('property.prop_id'))
    prop=db.relationship('Property',backref='proper')
    stud=db.relationship('Student',backref='dent')















    