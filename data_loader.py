# coding: gbk
import json
import pathlib

import pandas
from pandas.io.pytables import performance_doc

from structs import Student, ExamGroup, StudentGroup

tp = {
    "班级": int, "学号": int, "姓名": str,
    "语文": float, "数学": float, "英语": float,
    "物理": float, "化学": float, "生物": float,
    "政治": float, "历史": float, "地理": float
}
all_subjects = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理']

infos: dict[dict, dict[str, dict[str, float]]] = {}

ALL_EXAMS = ExamGroup("所有考试", [])
ALL_STUDENTS = StudentGroup("全体学生", [])


def get_single_exam(name):
    return ExamGroup(name, [name])


def get_single_student(cls, num, name):
    s = Student(name, num, cls)
    return StudentGroup(str(s), [s])


def get_class(cls: int):
    # 获取一个班级的学生组。
    stus = set()
    for i in ALL_STUDENTS.students:
        if i.cls == cls:
            stus.add(i)
    return StudentGroup(f"{cls}班", stus)


def try_load():
    global infos, ALL_EXAMS, ALL_STUDENTS
    dt_path = (pathlib.Path().absolute() / "data")
    dt_path.mkdir(exist_ok=True)
    tests = []
    students = []
    for i in dt_path.rglob("*.xlsx"):
        p = pandas.read_excel(str(i), dtype=tp, usecols=list(tp.keys()))
        tests.append(i.stem)
        for index, row in p.iterrows():
            student_info = Student(
                cls=row['班级'],
                num=row['学号'],
                name=row['姓名']
            )
            students.append(student_info)
            performance_info = {}
            for subject in all_subjects:
                if subject in p.columns and pandas.notna(row[subject]):
                    performance_info[subject] = row[subject]
                else:
                    performance_info[subject] = None  # 或者0.0，根据需求

            if student_info in infos:
                infos[student_info][i.stem] = performance_info
            else:
                infos[student_info] = {i.stem: performance_info}
    print(tests)
    ALL_EXAMS = ExamGroup("所有考试", tests)
    ALL_STUDENTS = StudentGroup("全体学生", students)
    # print(p)
