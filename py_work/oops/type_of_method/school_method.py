class Student:

    school_name ="ABC"

    def __init__(self,rol,name,total):

        self.rol =rol

        self.name=name

        self.total=total

    @classmethod

    def update_school_name(cls,name):

        cls.school_name = name

        print(cls.school_name)

    @staticmethod
    def is_pass(total):

        return True if total>140 else False



student_instance=Student(1000,"hari",145)

student_instance2=Student(1001,"vipin",135)


Student.update_school_name("CMS")

print(Student.is_pass(student_instance.total))
print(Student.is_pass(student_instance2.total))
        