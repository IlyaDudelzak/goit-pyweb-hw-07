from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship("Student", cascade="all, delete", backref="group")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE"))
    grades = relationship("Grade", cascade="all, delete", backref="student")

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
    subjects = relationship("Subject", cascade="all, delete", backref="teacher")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))
    grades = relationship("Grade", cascade="all, delete", backref="subject")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE"))