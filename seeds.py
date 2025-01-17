from models import Group, Student, Teacher, Subject, Grade
from connect_db import session
from random import choice, randint
import faker

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 1000
MIN_GRADE = 0
MAX_GRADE = 100

if __name__ == '__main__':
    groups = []
    students = []
    teachers = []
    subjects = []
    grades = []
    fake_data = faker.Faker("ru_RU")
    for _ in range(NUMBER_GROUPS):
        groups.append(Group(name=fake_data.word()))
        session.add(groups[_])
    for _ in range(NUMBER_STUDENTS):
        students.append(Student(fullname=fake_data.name(), group=choice(groups)))
        session.add(students[_])
    for _ in range(NUMBER_TEACHERS):
        teachers.append(Teacher(fullname=fake_data.name()))
        session.add(teachers[_])
    for _ in range(NUMBER_SUBJECTS):
        subjects.append(Subject(name=fake_data.job(), teacher=choice(teachers)))
        session.add(subjects[_])
    for _ in range(NUMBER_GRADES):
        grades.append(Grade(grade=randint(MIN_GRADE, MAX_GRADE), student=choice(students), subject=choice(subjects)))
        session.add(grades[_])
    session.commit()