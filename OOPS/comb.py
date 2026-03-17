class Classroom:
    def __init__(self):
        self.room_no = 101
        print("Classroom is created")

    def conduct_class(self):
        print("Class is going on")

class Teacher:
    def __init__(self, name):
        self.name = name
        print("Teacher is available")

    def teach(self):
        print(self.name, "is teaching")

class School:
    def __init__(self, name):
        self.sname = name

        self.classroom = Classroom()
        self.teacher = None
        print("School created with classroom")

    def assign_teacher(self, teacher_obj):
        self.teacher = teacher_obj
        print("Teacher assigned to classroom")


s = School("ABC School")

print(s.sname)
s.classroom.conduct_class()

t = Teacher("Ravi")
s.assign_teacher(t)

print(s.teacher.name)
s.teacher.teach()