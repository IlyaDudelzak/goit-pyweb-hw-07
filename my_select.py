from models import Group, Student, Teacher, Subject, Grade
from sqlalchemy import func, desc
from connect_db import session

def select_1():
    return session.query(
            Student.fullname, 
            func.round(func.avg(Grade.grade), 2)\
                .label('avg_grade')
            )\
            .select_from(Grade)\
            .join(Student)\
            .group_by(Student.id)\
            .order_by(desc('avg_grade'))\
            .limit(5).all()

def select_2():
    return session.query(
            Subject.name,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2)\
                .label('avg_grade')
        )\
        .join(Grade, Subject.id == Grade.subject_id)\
        .join(Student, Student.id == Grade.student_id)\
        .filter(Grade.subject_id == 2)\
        .group_by(Subject.name, Student.fullname)\
        .order_by(desc('avg_grade'))\
        .limit(1)\
        .one()

def select_3():
    return session.query(
            Subject.name, 
            Group.name, 
            func.round(func.avg(Grade.grade), 2)\
                .label('avg_grade')
            )\
            .select_from(Grade)\
            .join(Student, Student.id == Grade.student_id)\
            .join(Subject, Grade.subject_id == Subject.id)\
            .join(Group, Student.group_id == Group.id)\
            .filter(Grade.subject_id == 2)\
            .group_by(Group.id)\
            .order_by(desc('avg_grade'))\
            .all()
            
def select_4():
    return session.query(
            func.round(func.avg(Grade.grade), 2)\
                .label('avg_grade')
            )\
            .select_from(Grade)\
            .order_by(desc('avg_grade'))\
            .all()

def select_5():
    return session.query(
            Teacher.fullname,
            Subject.name
        )\
        .select_from(Grade)\
        .join(Subject, Subject.id == Grade.subject_id)\
        .join(Teacher, Teacher.id == Subject.teacher_id)\
        .filter(Teacher.id == 1)\
        .group_by(Subject.id)\
        .all()

def select_6():
    return session.query(Student.fullname,)\
            .select_from(Student)\
            .filter(Group.id == 1)\
            .order_by(Student.fullname)\
            .all()

def select_7():
    return session.query(
            Student.fullname,
            Subject.name, 
            Group.name, 
            Grade.grade
            )\
            .select_from(Grade)\
            .join(Student, Student.id == Grade.student_id)\
            .join(Subject, Subject.id == Grade.subject_id)\
            .join(Group, Group.id == Student.group_id)\
            .filter(Subject.id == 1, Group.id == 1)\
            .order_by(desc("grade"))\
            .all()

def select_8():
    return session.query(
            Teacher.fullname,
            Subject.name,
            func.round(func.avg(Grade.grade), 2)\
                .label('avg_grade')
        )\
        .select_from(Grade)\
        .join(Subject, Subject.id == Grade.subject_id)\
        .join(Teacher, Teacher.id == Subject.teacher_id)\
        .filter(Teacher.id == 1)\
        .group_by(Subject.id)\
        .all()

def select_9():
    return session.query(
            Student.fullname,
            Subject.name,
            )\
            .select_from(Grade)\
            .join(Student, Student.id == Grade.student_id)\
            .join(Subject, Subject.id == Grade.subject_id)\
            .filter(Student.id == 3)\
            .group_by(Subject.id)\
            .order_by(Subject.id)\
            .all()  

def select_10():
    return session.query(
            Subject.name,
            Student.fullname,
            Teacher.fullname
            )\
            .select_from(Grade)\
            .join(Student, Student.id == Grade.student_id)\
            .join(Subject, Subject.id == Grade.subject_id)\
            .join(Teacher, Teacher.id == Subject.teacher_id)\
            .filter(Student.id == 3, Teacher.id == 1)\
            .group_by(Subject.id)\
            .order_by(Subject.id)\
            .all()  

if __name__ == '__main__':
    print(select_1(), end="\n\n")
    print(select_2(), end="\n\n")
    print(select_3(), end="\n\n")
    print(select_4(), end="\n\n")
    print(select_5(), end="\n\n")
    print(select_6(), end="\n\n")
    print(select_7(), end="\n\n")
    print(select_8(), end="\n\n")
    print(select_9(), end="\n\n")
    print(select_10(), end="\n\n")