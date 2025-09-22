class stud:

    id:int

    name:str

    course:str

    def set_student(self,id,name,course):

        self.id=id

        self.name=name

        self.course=course

    def display_student(self):

        print(self.id,self.name,self.course)


stud_instance=stud()

stud_instance.set_student(102,"nami","django")

stud_instance.display_student()