from dataclasses import dataclass

import data_loader


class Student:
    name: str
    num: int
    cls: int

    def __init__(self, name, num, cls):
        self.name = name
        self.num = num
        self.cls = cls

    def __str__(self):
        return f"{self.cls:02d}{self.num:02d} {self.name}"

    def __repr__(self):
        return f"<Stu {self.cls:02d}{self.num:02d} {self.name}>"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.num == other.num and self.cls == other.cls

    def __hash__(self):
        return hash((self.name, self.num, self.cls))

@dataclass
class ExamGroup:
    name: str
    exams: list[str]  # 考试名称列表

    def __init__(self, name, exams):
        self.name = name
        self.exams = exams

    def size(self) -> int:
        return len(self.exams)


@dataclass
class StudentGroup:
    name: str
    students: set[Student]

    def __init__(self, name: str, students: set[Student]):
        self.name = name
        self.students = students

    def size(self) -> int:
        return len(self.students)

    def get_med(self, exams: ExamGroup, subjects: list[str]):
        # 获得一些考试的中位分数
        # 返回格式: {subject1: score1, subject2: score2 ...}
        ret = {}
        for i in subjects:
            ret[i] = list()

        for i in exams.exams:
            for j in self.students:
                for k in data_loader.infos[j][i]:
                    if k in subjects:
                        ret[k].append(data_loader.infos[j][i][k])

        for i in ret:
            ret[i] = sorted(ret[i])
            l = len(ret[i])
            if l % 2 == 0:
                ret[i] = (ret[i][l//2] + ret[i][l//2+1])/2
            else:
                ret[i] = ret[i][l//2]

        return ret

    def get_avgs(self, exams: ExamGroup, subjects: list[str]):
        # 获得一些考试的平均分数
        # 返回格式: {subject1: score1, subject2: score2 ...}
        ret = dict.fromkeys(subjects, 0)
        cnt = dict.fromkeys(subjects, 0)
        for i in exams.exams:
            for j in self.students:
                for k in data_loader.infos[j][i]:
                    if k in subjects:
                        ret[k] += data_loader.infos[j][i][k]
                        cnt[k] += 1
        for i in ret:
            ret[i] /= cnt[i]
            ret[i] = round(ret[i], 1)
        return ret

    def get_dot(self, exam: str, subjects: list[str]):
        # 获得学生的分数分布
        # 返回格式: {score1: count1, score2: count2...}
        ret = {}
        for i in self.students:
            for j in data_loader.infos[i][exam]:
                tot = 0
                if j in subjects:
                    tot += data_loader.infos[i][exam][j]
                if tot in ret:
                    ret[tot] += 1
                else:
                    ret[tot] = 1
        return ret

    def get_student_names(self) -> list[str]:
        return [stu.name for stu in self.students]

